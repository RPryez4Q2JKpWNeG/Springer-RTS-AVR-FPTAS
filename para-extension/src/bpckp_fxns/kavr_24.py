"""Paper-based implementation of Bijinemula et al. RTSS '18"""

import copy
import sys  #Exit command
import multiprocessing

from time import perf_counter #hi-res clock
from math import sqrt   #sqrt
from utilities import delta_mode_allocator
from collections import defaultdict #Dictionary that does not throw KeyErrors
sys.path.append("..")

#parallelization_type
#0 = Parallel delta - grouped
#1 = Parallel mode - single

class Kavr2024:

    """KAVR AVR Task Demand BPCKP Solver"""

    def __init__(self, avr_task_instance, precision, memoization, give_sln_seq, verbose_print_level, n_cores,parallelization_type):

        self.precision = precision
        self.memoization = memoization
        self.give_sln_seq = give_sln_seq
        self.verbose_print_level = verbose_print_level
        self.n_cores = n_cores
        assert self.n_cores > 0
        self.parallelization_type = parallelization_type
        self.dict_max_demand_local = defaultdict(dict)

        self.counter_dict_max_demand = 0
        self.counter_dict_max_demand_memo = 0

        #Dictionary for logging speeds, completion times - Supports dynamic programming.
        self.dict_max_demand = defaultdict(dict)
        self.avr_task_instance = avr_task_instance

        #Timekeeping
        self.parallelized_deltas_start_time_s = -1
        self.parallelized_modes_start_time_s = -1

        #RB Speeds
        self.rbs_arr = []

        #Units
        #a_max, a_min : revolutions / min^2
        #speed, peak_speed, speed_new : revolutions / minute (RPM)

        #Acceleration equal in magnitude to deceleration per Bijinemula et al. Sec. III.A Para. 4
        a_max = self.avr_task_instance.alpha
        a_min = -a_max

        #Execution time values (micro seconds)
        # from Mohaqeqi et al. Table 18 - http://user.it.uu.se/~yi/pdf-files/2017/ecrts17.pdf
        wcet_arr = copy.deepcopy(self.avr_task_instance.wcet)
        wcet_arr.remove(0)

        #Sort RB Speeds in increasing order
        omega_arr = self.avr_task_instance.omega

        #Sort execution times in decreasing order
        wcet_arr.sort(reverse=True)

        #Validate # RB Speeds is one more than # Execution Times
        if len(omega_arr) != len(wcet_arr)+1:
            print('Error: The # boundary speeds != # WCETs + 1.')
            sys.exit(0)

        #Print Parameters:
        # print('omega_arr: ',omega_arr, 'revolutions / minute')
        # print('wcet_arr: ',wcet_arr, 'us')
        # print('a_max:          ',a_max, ' revolutions / min^2')
        # print('a_min:          ',a_min, 'revolutions / min^2')

        #Push terms to global
        self.omega_arr = omega_arr
        self.wcet_arr = wcet_arr
        self.a_max = a_max
        self.a_min = a_min

    def min_rotation_time(self,omega):

        """Get fastest MIAT achievable for job released at speed \\omega"""

        alpha_max = self.a_max

        #Fastest reachable speed
        max_speed_no_limit = sqrt(omega**2 + 2*alpha_max)
        max_speed_limit_by_omega_m = min(max_speed_no_limit,self.omega_arr[-1])

        #MIAT to fastest reachable speed
        miat_sec = self.calc_min_time(omega,max_speed_limit_by_omega_m)

        return miat_sec

    def calc_min_time(self,speed,speed_new):

        """Calculate MIAT between two speeds"""

        #setup vars like Bijinemula et. al. Eqn 3.
        omega = speed
        f = speed_new
        alpha_max = self.a_max

        #Bijinemula et. al. Eqn 3
        omega_p = sqrt((omega**2+f**2+self.a_max)/2)

        #setup vars like Bijinemula et. al. Eqn 4
        omega_max = self.omega_arr[-1]

        #Bijinemula et. al. Eqn 4
        if omega_p <= omega_max:

            miat_min = (sqrt(2*omega**2 + 2*f**2 + 4*alpha_max) - omega - f)/alpha_max

        else:

            miat_min = ((omega_max - f - omega)/(alpha_max)) + ((omega**2 + f**2)/(2*omega_max*alpha_max)) + (1/omega_max)

        #Get miat in seconds
        miat_sec = miat_min * 60

        #Return minimum time in seconds
        return miat_sec

    def c(self,omega):

        """Get WCET for jobs released at speed \\omega"""

        wcet = -1

        for i in range(len(self.omega_arr)):

            if omega <= self.omega_arr[i]:

                wcet =  self.wcet_arr[i-1]
                break

        return wcet

    def next_possible_speeds(self,speed):

        """Get the set of reachable speeds from 'speed'
        (i.e., get the set of equivalent or higher speed RBs and the maximum reachable speed)"""

        # if speed in dict_nps:
        #     return dict_nps[speed]

        nps = []

        alpha_max = self.a_max

        max_speed_no_limit  = sqrt(speed**2 + 2*alpha_max)
        max_speed_limit_by_omega_m = min(max_speed_no_limit,self.omega_arr[-1])

        for rbs_x in self.omega_arr:

            if speed <= rbs_x <= max_speed_limit_by_omega_m:

                nps += [rbs_x]

        if max_speed_limit_by_omega_m != self.omega_arr[-1]:
            nps += [max_speed_limit_by_omega_m]

        return nps

    #Function for calculating maximum demand given an initial speed over a set duration of time
    # - Bijinemula et al. Algorithm 1
    def calculate_demand(self, omega, delta):

        """Calculate maximum demand that can be generated by a sequence of speeds
        beginning at speed \\omega over an interval of side \\delta seconds"""

        self.counter_dict_max_demand += 1

        #Initialization
        max_demand = 0
        max_seq = []

        # delta_rounded = delta
        if self.precision == 0:
            delta_rounded = delta
        else:
            delta_rounded = round(delta,self.precision)

        #Stored demand check
        if self.memoization:
            memo_answer = None
            if omega in self.dict_max_demand_local.keys():
                if delta_rounded in self.dict_max_demand_local[omega].keys():
                    memo_answer = self.dict_max_demand_local[omega][delta_rounded]
            if memo_answer is not None:
                self.counter_dict_max_demand_memo += 1
                return memo_answer

        #If remaining time is less than minimum rotation time...
        if delta_rounded < self.min_rotation_time(omega):

            #No demand generated
            return (max_demand,max_seq)

        current_speed_wcet = self.c(omega)

        #For every reachable speed...
        for omega_prime in self.next_possible_speeds(omega):

            miat_omega_to_omega_prime = self.calc_min_time(omega,omega_prime)
            delta_remaining = delta_rounded - miat_omega_to_omega_prime

            (ret_demand_calc_d,ret_seq_calc_d) = self.calculate_demand(omega_prime,delta_remaining)
            demand_omega_prime = current_speed_wcet + ret_demand_calc_d

            if self.give_sln_seq:

                if ret_seq_calc_d == []:
                    seq = [[round(omega,2),1]]
                else:
                    if ret_seq_calc_d[0][0] == round(omega,2):
                        seq = ret_seq_calc_d
                        seq[0][1] +=1
                    else:
                        seq = [[round(omega,2),1]] + ret_seq_calc_d
            else:

                seq = []

            if demand_omega_prime > max_demand:
                max_demand = demand_omega_prime
                max_seq = seq

        if self.memoization:
            self.dict_max_demand_local[omega][delta_rounded] = (max_demand,max_seq)

        return (max_demand,max_seq)

    def calculate_exact_demand(self,delta_list):

        """Get exact demand for AVR task given list of \\delta window sizes"""

        sys.setrecursionlimit(3000)

        if self.n_cores > 1:
            if self.parallelization_type == 0:
                (delta_table,delta_table_creation_time_s) = self.calculate_exact_demand_parallelize_deltas(delta_list)
            else:
                (delta_table,delta_table_creation_time_s) = self.calculate_exact_demand_parallelize_modes(delta_list)
        else:
            (delta_table,delta_table_creation_time_s) = self.calculate_exact_demand_uniprocessor_deltas(delta_list)

        return (delta_table,delta_table_creation_time_s)

    def calculate_exact_demand_parallelize_modes(self,delta_list):

        """Get exact demand for AVR task given list of \\delta window sizes parallelizing modes in groups"""

        if self.verbose_print_level >=1:
            print("Method: KAVR'24")

        self.parallelized_modes_start_time_s = perf_counter()

        #Get num nodes (num_deltas)
        num_deltas = len(delta_list)
        delta_table = [[-1 for i in range(4)] for j in range(num_deltas)]

        #Create results arrays
        process_results = [-1]*self.n_cores
        results_array = [-1]*self.n_cores

        #Create process pool
        pool = multiprocessing.Pool(processes=self.n_cores)

        #Find the maximum usable cores
        usable_cores_maximum = min(self.n_cores,len(self.omega_arr))

        #Construct sub arrays
        sub_arrays = delta_mode_allocator.delta_allocator(self.omega_arr,self.n_cores)

        #For every sub array...
        for i in range(usable_cores_maximum):

            #Parallelize
            process_results[i] = pool.apply_async(self.calculate_exact_demand_seq_mode_list, args=(delta_list,sub_arrays[i],))

        for i in range(usable_cores_maximum):
            results_array[i] = process_results[i].get()

        pool.close()
        pool.join()

        #For every result...
        for d in range(num_deltas):
            max_demand = 0
            max_demand_id = -1

            for i in range(usable_cores_maximum):

                if results_array[i][d][1] > max_demand:
                    max_demand_id = i
                    max_demand = results_array[i][d][1]

            delta_table[d] = results_array[max_demand_id][d]

        parallelized_modes_end_time_s = perf_counter()
        delta_table_creation_time_s = parallelized_modes_end_time_s - self.parallelized_modes_start_time_s

        #Calculate individual times
        #For every demand interval...
        for d in range(num_deltas):

            individual_time = 0     #Assume individual time is zero

            for i in range(usable_cores_maximum):   #For every processor...
                individual_time = max(results_array[i][d][2],individual_time)   #Add individual processing time for this demand interval

            delta_table[d][2] = individual_time     #Assign individual demand interval processing time

            cumulative_time = 0

            for i in range(usable_cores_maximum):   #For every processor...
                cumulative_time = max(results_array[i][d][3],cumulative_time)

            delta_table[d][3] = cumulative_time

        return (delta_table,delta_table_creation_time_s)

    def calculate_exact_demand_seq_mode_list(self,delta_list,mode_list):

        """Calculate max demand for all \\delta starting at modes in mode_list"""

        num_deltas = len(delta_list)
        num_modes = len(mode_list)

        delta_table = [[-1 for i in range(4)] for j in range(num_deltas)]

        for d in range(num_deltas):

            start_s = perf_counter()

            delta_us = delta_list[d]
            delta_s = delta_us / 1_000_000

            max_pattern = (0,[0])
            max_demand = 0

            #For each node
            for i in range(num_modes):

                #Calculate maximum demand starting from the selected node
                returned_package = self.calculate_demand(mode_list[i],delta_s)
                demand = returned_package[0]
                pattern = returned_package[1]

                #Update maximum demand if needed
                if demand > max_demand:
                    max_demand = demand
                    max_pattern = pattern

            end_s = perf_counter()

            individual_delta_runtime_s = end_s - start_s
            cumulative_delta_runtime_s = end_s - self.parallelized_modes_start_time_s

            if self.verbose_print_level >=2:
                output = "KAVR Delta " + str(d+1) + " of " + str(len(delta_list))
                output += " | Delta: " + str(int(delta_us))
                output += " D(us): " + str(max_demand)
                output += " RT(s): " + str(individual_delta_runtime_s)
                if self.give_sln_seq:
                    output += " P: " + str(max_pattern)
                print(output)

            #Log results
            delta_table[d][0] = delta_us
            delta_table[d][1] = max_demand
            delta_table[d][2] = individual_delta_runtime_s
            delta_table[d][3] = cumulative_delta_runtime_s

        return delta_table

    def calculate_exact_demand_uniprocessor_deltas(self,delta_list):
        """Get exact demand for AVR task given list of \\delta window sizes without parallelizing \\deltas"""

        if self.verbose_print_level >=1:
            print("Method: KAVR'24")

        start_time_cumulative = perf_counter()

        num_deltas = len(delta_list)
        delta_table = [[-1 for i in range(4)] for j in range(num_deltas)]

        ##Recursive Demand Calculation
        #Initialization
        max_demand = 0

        #For every 0.01 time step in [0.01,1.01)
        for d in range(num_deltas):

            delta = delta_list[d]

            #Convert to seconds
            delta = delta/1000000

            tot_time = delta

            start = perf_counter()

            max_pattern = (0,[0])

            #For every RB speed
            for rbs in self.omega_arr:

                #Calculate maximum demand starting from selected RB
                # print("Time:", tot_time, "Try: ",i)
                returned_package = self.calculate_demand(rbs,tot_time)
                demand = returned_package[0]
                pattern = returned_package[1]
                # print("\n")

                #Update maximum demand if needed
                if demand > max_demand:
                    max_demand = demand
                    max_pattern = pattern

            end = perf_counter()
            total_time = end - start
            cumulative_time = end - start_time_cumulative
            # output = "\delta = " + str(tot_time) + " D: "
            # output += str(max_demand) + " in " + str(round(total_time,2))
            # print(output)

            if self.verbose_print_level >=2:
                # time_remaining = max_pattern[-1][0]
                # time_spent = delta - time_remaining
                output = "KAVR Delta " + str(d+1) + " of " + str(len(delta_list))
                output += " | Delta: " + str(int(delta*1000*1000))
                # output +=" MIAT(us) " + str(round(time_spent*1000*1000,2))
                output += " D(us): " + str(max_demand)
                output += " RT(s): " + str(total_time)
                if self.give_sln_seq:
                    output += " P: " + str(max_pattern)
                print(output)
            #If verbose requested write the demand for this time-step to file
            # if args.verbose:
            # f.write('Max demand for time: {} = {}\n'.format(tot_time,max_demand))

            delta_table[d][0] = delta
            delta_table[d][1] = max_demand
            delta_table[d][2] = total_time
            delta_table[d][3] = cumulative_time

        uniprocessor_sequential_delta_table_creation_time_s = delta_table[-1][3]

        if self.verbose_print_level >= 1:
            print("Gets/Total:", self.counter_dict_max_demand_memo,"/",self.counter_dict_max_demand)

        return (delta_table,uniprocessor_sequential_delta_table_creation_time_s)

    def calculate_exact_demand_parallelize_deltas(self,delta_list):

        """Get exact demand for AVR task given list of \\delta window sizes parallelizing \\deltas in groups"""

        if self.verbose_print_level >=1:
            print("Method: KAVR'24")

        self.parallelized_deltas_start_time_s = perf_counter()

        #Get num nodes (num_deltas)
        num_deltas = len(delta_list)
        delta_table = [[-1 for i in range(4)] for j in range(num_deltas)]

        #Create results arrays
        process_results = [-1]*self.n_cores
        result_delta_tables = [-1]*self.n_cores
        result_delta_table_creation_times = [-1]*self.n_cores

        #Create process pool
        pool = multiprocessing.Pool(processes=self.n_cores)

        #Find the maximum usable cores
        usable_cores_maximum = min(self.n_cores,len(self.omega_arr))

        #Construct sub arrays
        sub_arrays = delta_mode_allocator.delta_allocator(delta_list,self.n_cores)

        #For every subarray...
        for i in range(usable_cores_maximum):

            #Parallelize
            process_results[i] = pool.apply_async(self.calculate_exact_demand_uniprocessor_deltas, args=(sub_arrays[i],))

        #For each node, update maximum package
        for i in range(usable_cores_maximum):
            (result_delta_tables[i],result_delta_table_creation_times[i]) = process_results[i].get()

        pool.close()
        pool.join()

        #For every result...
        for i in range(usable_cores_maximum):
            if i == 0:
                delta_table = result_delta_tables[i]
            else:
                delta_table += result_delta_tables[i]

        delta_table = sorted(delta_table)

        parallelized_deltas_end_time_s = perf_counter()
        delta_table_creation_time_s = parallelized_deltas_end_time_s - self.parallelized_deltas_start_time_s

        if self.verbose_print_level >= 1:
            print("Gets/Total:", self.counter_dict_max_demand_memo,"/",self.counter_dict_max_demand)

        return (delta_table,delta_table_creation_time_s)
