"""Implementation of Mohaqeqi et al. AVR task DBF algorithm"""

#Dependencies
from time import perf_counter           #clock w/ highest resolution
from math import sqrt                   #Square root
from bisect import bisect_left          #Provides would-be index of element to insert
from collections import defaultdict     #Default dictionary
from utilities import delta_mode_allocator
import sys                              #Exit command
import copy
import datetime
import multiprocessing

#pylint: disable=C0200,C0201
#pylint: disable=line-too-long

#self.parallelization_type
#0 = Parallel delta - grouped
#1 = Parallel mode - grouped

class Row2017:

    """ROW17 AVR Task Demand Solver"""

    def __init__(self,avr_task_instance,precision,memoization,give_sln_seq,verbose_print_level,n_cores, parallelization_type):

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

        self.avr_task_instance = avr_task_instance

        self.start_time_cumulative_s = -1
        self.parallelized_deltas_start_time_s = -1
        self.parallelized_modes_start_time_s = -1

        #Units
        #A_MAX, A_MIN - revolutions / min^2
        #speed, peak_speed, speed_new - revolutions / minute (RPM)

        #Acceleration equal in magnitude to deceleration per Bijinemula et al. Sec. III.A Para. 4
        self.a_max = self.avr_task_instance.alpha
        self.a_min = -self.a_max

        #Execution time values (micro seconds) from Mohaqeqi et al. Table 18 - http://user.it.uu.se/~yi/pdf-files/2017/ecrts17.pdf
        self.wcet_arr = copy.deepcopy(self.avr_task_instance.wcet)
        self.wcet_arr.remove(0)

        #Sort Right Boundary Speeds in increasing order
        self.omega_arr = self.avr_task_instance.omega
        self.omega_arr_squared = -1

        self.adjacency_matrix = -1
        self.nodes = -1

        self.returned_package_shared_mem = []

        #Validate # Right Boundary Speeds is one more than # Execution Times
        if len(self.omega_arr) != len(self.wcet_arr)+1:
            print('Error: The number of boundary speeds should be one more than the number of execution times.')
            sys.exit(0)

    #Function for calculating maximum demand given a starting node over a set duration of time
    def calc_demand(self,i,time):

        """Calculate maximum demand when starting a speed sequence at vertex i
        over an interval of size 'time' (in seconds)"""

        self.counter_dict_max_demand += 1

        #Initialization
        demand_max = 0
        seq_max = []

        if self.precision == 0:
            time_rounded = time
        else:
            time_rounded = round(time,self.precision)

        #Stored demand check
        if self.memoization:
            memo_answer = None
            if i in self.dict_max_demand_local.keys():
                if time_rounded in self.dict_max_demand_local[i].keys():
                    memo_answer = self.dict_max_demand_local[i][time_rounded]
            if memo_answer is not None:
                self.counter_dict_max_demand_memo += 1
                return memo_answer

        #If node is not the first right boundary speed...
        if self.nodes[i][1]!=self.omega_arr_squared[0]:
            #Assign execution time based on index
            dem_node = self.wcet_arr[bisect_left(self.omega_arr_squared,self.nodes[i][1])-1]
        #...otherwise, assign first execution time
        else:
            dem_node = self.wcet_arr[0]

        #Iterate through all nodes
        for j in range(len(self.nodes)):

            #If the node pair selected is reachable from each other...
            if (i,j) in self.adjacency_matrix.keys():

                #Extract the time required to reach the next node
                time_next_node = self.adjacency_matrix[(i,j)]

                #If insufficient time remains to reach the next node...
                if time_rounded - time_next_node < 0:
                    #Do not count towards demand, try next node
                    continue

                #If time remaining is exactly the required time...
                if time_rounded - time_next_node == 0:
                    #Update demand if necessary and continue
                    if dem_node > demand_max:
                        demand_max = dem_node
                        continue

                #Calculate new demand
                (ret_demand_calc_d,ret_seq_calc_d) = self.calc_demand(j,time_rounded-time_next_node)
                demand = dem_node + ret_demand_calc_d

                if self.give_sln_seq:
                    if ret_seq_calc_d == []:
                        seq = [[round(sqrt(self.nodes[i][1]),2),1],time_rounded-time_next_node]
                    else:
                        if ret_seq_calc_d[0][0] == round(sqrt(self.nodes[i][1]),2):
                            seq = ret_seq_calc_d
                            seq[0][1] += 1
                        else:
                            seq = [[round(sqrt(self.nodes[i][1]),2),1]] + ret_seq_calc_d
                else:
                    seq = []

                #Update demand if necessary
                if demand > demand_max:
                    demand_max = demand
                    seq_max = seq

        #Update hash table with max demand and return
        if self.memoization:
            self.dict_max_demand_local[i][time_rounded] = (demand_max,seq_max)

        return (demand_max,seq_max)

    def delta_iterator_setup(self):

        """Create nodes required for ROW'17 to run"""

        a_max = self.a_max
        a_min = self.a_min

        #Start timer
        self.start_time_cumulative_s = perf_counter()

        #Boundary Speeds
            #Squares of right boundary speeds used to avoid repeated sqrt computation later
            #Speeds in the first step are not counted per Lemma 2 - start from first right boundary speed
        self.omega_arr_squared = [speed**2 for speed in self.omega_arr]
        max_speed = self.omega_arr_squared[-1]

        #Setup node_speeds
        node_speeds = set()

        #Iterate through all boundary speeds, creating nodes for all reachable speeds
        for x in range(len(self.omega_arr_squared)):
            speed = self.omega_arr_squared[x]           #Select boundary speed
            while speed <= max_speed:            #While speed has not exceed max speed
                node_speeds.add(speed)               #Create node for speed
                speed = speed + 2*a_max             #Add subsequent, increasing speed via a_max

            speed = self.omega_arr_squared[x]           #Select boundary speed
            while speed>=self.omega_arr_squared[0]:     #While speed has not fallen below the lowest boundary speed
                node_speeds.add(speed)               #Create node for speed
                speed = speed + 2*a_min             #Add subsequent, decreasing speed via a_min
        node_speeds = sorted(node_speeds)         #Nodes sorted by speed increasing order

        #Setup nodes
        self.nodes = []

        for i,j in zip(node_speeds[:-1],node_speeds[1:]): #For each tuple in a list of created tuples
            self.nodes.append((i,j))                             #Add each tuple to nodes

        self.adjacency_matrix = dict()  #Empty adjacency matrix for creating DRT graph

        for i in range(len(self.nodes)):                 #For every node tuple
            current_node = self.nodes[i][1]                     #Select right boundary
            for j in range(i,len(self.nodes)):               #Iterate through all possible next right boundaries
                next_node = self.nodes[j][1]                        #Select next right boundary
                max_reach = current_node + 2*a_max              #Calculate maximum next speed

                #If next right boundary is not reachable, break
                if next_node > max_reach:
                    break

                #If next right boundary is reachable via constant a_max...
                if next_node == max_reach:
                    #Calculate minimum interarrival time - Mohaqeqi et al. Sec. 3.2 Case 2
                    self.adjacency_matrix[(i,j)] = 60*(sqrt(next_node)-sqrt(current_node))/a_max

                #...otherwise, the next right boundary is reachable via variable acceleration
                else:
                    #Calculate the prospective peak speed
                    mid_speed = (2*a_min*a_max+a_min*current_node-a_max*next_node)/(a_min-a_max)

                    #If the prospective peak speed does not exceed maximum speed...
                    if mid_speed <= max_speed:
                        #Calculate3 minimum interarrival time in seconds - Mohaqeqi et al. Sec 3.2 Eqn 20
                        self.adjacency_matrix[(i,j)] = 60*((sqrt(mid_speed)-sqrt(current_node))/a_max +(sqrt(next_node)-sqrt(mid_speed))/a_min)

                    #...otherwise, the prospective peak speed exceeds maximum speed
                    else:
                        #Calculate the time to reach maximum speed - Mohaqeqi et al. Sec. 3.2 Eqn 21 t_1^*
                        t1 = (sqrt(max_speed) - sqrt(current_node))/a_max
                        #Calculate the time over which maximum speed is maintained - Mohaqeqi et al. Sec. 3.2 Eqn 21 t_2^*
                        t2 = (1-((max_speed-current_node)/(2*a_max))-((next_node-max_speed)/(2*a_min)))/sqrt(max_speed)
                        #Calculate the time to descend from maximum speed to final speed - Mohaqeqi et al. Sec. 3.2 Eqn 21 t_3^*
                        t3 = (sqrt(next_node)-sqrt(max_speed))/a_min

                        #Sum individual time segments and convert to seconds
                        self.adjacency_matrix[(i,j)] = 60*(t1 + t2 + t3)

                #Mirror adjacency matrix
                self.adjacency_matrix[(j,i)] = self.adjacency_matrix[(i,j)]

    def calculate_exact_demand(self,delta_list):

        """Get exact demand for AVR task given list of \\delta window sizes"""

        self.delta_iterator_setup()

        sys.setrecursionlimit(2000)

        if self.n_cores > 1:
            if self.parallelization_type == 0:
                (delta_table,delta_table_creation_time_s) = self.calculate_exact_demand_parallelize_deltas(delta_list)
            else:
                (delta_table,delta_table_creation_time_s) = self.calculate_exact_demand_parallelize_modes(delta_list)
        else:
            (delta_table,delta_table_creation_time_s) = self.calculate_exact_demand_sequential_deltas(delta_list)

        return (delta_table,delta_table_creation_time_s)

    def calculate_exact_demand_parallelize_modes(self,delta_list):

        """Get exact demand for AVR task given list of \\delta window sizes parallelizing modes in groups"""

        if self.verbose_print_level >=1:
            print("Method: ROW'17")

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
        sub_arrays = delta_mode_allocator.node_allocator(len(self.nodes),self.n_cores)

        #For every sub array...
        for i in range(usable_cores_maximum):

            #Parallelize
            process_results[i] = pool.apply_async(self.calculate_exact_demand_single_mode, args=(delta_list,sub_arrays[i],))

        #For each node, update maximum package
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
                individual_time = max(results_array[i][d][2],individual_time)  #Take the max individual time for this \\delta

            delta_table[d][2] = individual_time     #Assign individual demand interval processing time

            cumulative_time = 0

            for i in range(usable_cores_maximum):   #For every processor...
                cumulative_time = max(results_array[i][d][3],cumulative_time)

            #Mark cumulative as negative
            delta_table[d][3] = cumulative_time

        return (delta_table,delta_table_creation_time_s)

    def calculate_exact_demand_single_mode(self,delta_list,mode_list):

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
                returned_package = self.calc_demand(mode_list[i],delta_s)
                demand = returned_package[0]
                pattern = returned_package[1]

                #Update maximum demand if needed
                if demand > max_demand:
                    max_demand = demand
                    max_pattern = pattern

            end_s = perf_counter()

            individual_delta_runtime_s = end_s - start_s
            cumulative_delta_runtime_s = end_s - self.start_time_cumulative_s

            #Print details if desired
            if self.verbose_print_level >=2:
                output = "ROW Delta " + str(d+1) + " of " + str(len(delta_list))
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

    def calculate_exact_demand_parallelize_deltas(self,delta_list):

        """Get exact demand for AVR task given list of \\delta window sizes parallelizing \\deltas in groups"""

        if self.verbose_print_level >=1:
            print("Method: ROW'17")

        self.parallelized_deltas_start_time_s = perf_counter()

        #Get num nodes (num_deltas)
        num_deltas = len(delta_list)
        delta_table = [[-1 for i in range(4)] for j in range(num_deltas)]

        #Create results arrays
        process_results = [-1]*self.n_cores
        results_array = [-1]*self.n_cores
        cumulative_time_results = [-1]*self.n_cores

        #Create process pool
        pool = multiprocessing.Pool(processes=self.n_cores)

        #Find the maximum usable cores
        usable_cores_maximum = min(self.n_cores,len(self.omega_arr))

        #Construct sub arrays
        sub_arrays = delta_mode_allocator.delta_allocator(delta_list,self.n_cores)

        #For every sub array...
        for i in range(usable_cores_maximum):

            #Parallelize
            process_results[i] = pool.apply_async(self.calculate_exact_demand_sequential_deltas, args=(sub_arrays[i],))

        #For each node, update maximum package
        for i in range(usable_cores_maximum):
            (results_array[i],cumulative_time_results[i]) = process_results[i].get()

        pool.close()
        pool.join()

        #For every result...
        for i in range(usable_cores_maximum):
            if i == 0:
                delta_table = results_array[i]
            else:
                delta_table += results_array[i]

        delta_table.sort()

        parallelized_deltas_end_time_s = perf_counter()
        delta_table_creation_time_s = parallelized_deltas_end_time_s - self.parallelized_deltas_start_time_s

        return (delta_table,delta_table_creation_time_s)

    def calculate_exact_demand_single_delta(self,delta_s):

        """Calculate demand for a single time interval, \\delta"""

        start_s = perf_counter()

        max_pattern = (0,[0])
        max_demand = -1

        #For each node
        for i in range(len(self.nodes)):

            #Calculate maximum demand starting from the selected node
            returned_package = self.calc_demand(i,delta_s)
            demand = returned_package[0]
            pattern = returned_package[1]

            #Update maximum demand if needed
            if demand > max_demand:
                max_demand = demand
                max_pattern = pattern

        #End performance counting, calculate and log total time
        end_s = perf_counter()
        individual_delta_runtime_s = end_s - start_s
        cumulative_delta_runtime_s = end_s - self.start_time_cumulative_s

        return (max_demand,max_pattern,individual_delta_runtime_s,cumulative_delta_runtime_s)

    def calculate_exact_demand_sequential_deltas(self,delta_list):

        """Get exact demand for AVR task given list of \\delta window sizes"""

        if self.verbose_print_level >=1:
            print("Method: ROW'17")

        num_deltas = len(delta_list)
        delta_table = [[-1 for i in range(4)] for j in range(num_deltas)]

        max_demand = 0

        self.start_time_cumulative_s = perf_counter()

        #For every interval length...
        for d in range(num_deltas):

            #Select time
            delta_us = delta_list[d]
            delta_s = delta_us/1000000

            (max_demand,max_pattern,individual_runtime_s,cumulative_runtime_s) = self.calculate_exact_demand_single_delta(delta_s)

            #Print details if desired
            if self.verbose_print_level >=2:
                output = "ROW Delta " + str(d+1) + " of " + str(len(delta_list))
                output += " | Delta: " + str(int(delta_us))
                output += " D(us): " + str(max_demand)
                output += " RT(s): " + str(individual_runtime_s)
                if self.give_sln_seq:
                    output += " P: " + str(max_pattern)
                print(output)

            #Log results
            delta_table[d][0] = delta_us
            delta_table[d][1] = max_demand
            delta_table[d][2] = individual_runtime_s
            delta_table[d][3] = cumulative_runtime_s

        end_time_cumulative_s = perf_counter()
        cumulative_runtime_s = self.start_time_cumulative_s - end_time_cumulative_s

        #Print details if desired
        if self.verbose_print_level >= 1:
            print("Gets/Total:", self.counter_dict_max_demand_memo,"/",self.counter_dict_max_demand)

        #Return results for all intervals
        return (delta_table,cumulative_runtime_s)

    def create_fn_w_timestamp(self,base):
        """Create file name with timestamp"""

        today = datetime.date.today()               #Get date
        postfix = "-" + str(today)                  #Add formatted date
        now = datetime.datetime.now()               #Get Time
        current_time = now.strftime("%H-%M-%S")     #Convert time to formatted string
        postfix += "-" + str(current_time)          #Add formatted time to filename
        postfix += ".txt"                           #Append suffix
        prefix = "exp_data/"                        #Create prefix
        full_file_name = prefix + base + postfix    #Append directory
        file_name = base + postfix
        return (full_file_name,file_name,prefix,postfix)        #Return completed Filename
