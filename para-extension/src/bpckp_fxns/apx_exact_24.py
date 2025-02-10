"""
Predefined Sequence (PDS)
Based Bounded Precedence Constraint Knapsack (BPCKP)
FPTAS for AVR Task Demand
Functions
"""
#pow,floor,ceiling
import math
import multiprocessing

#Performance counter - clock with highest available resolution
from time import perf_counter
from utilities import time_conversions
from utilities import delta_mode_allocator
from avr_fxns import avr_task as AVR_TASK

#pylint: disable=C0200,C0301,C0302

RETURN_PACKAGE_ROUNDING_PRECISION = 12
USE_RET_PACKAGE = 0

USE_OMEGA_ASSERTS = 0
USE_ASSERTS = 0
USE_DICT_PEAK_SPEED_RPM_RPM = 1

#self.parallelization_type
#0 = Parallel delta - grouped
#1 = Parallel mode - grouped

class ApxExact24:

    """
    Predefined Sequence (PDS)
    Based Bounded Precedence Constraint Knapsack (BPCKP)
    FPTAS for AVR Task Demand
    Functions
    """

    def __init__(self,avr_task_instance,avr_apx,n_cores,parallelization_type):

        self.t_avr = avr_task_instance
        self.avr_apx = avr_apx
        self.max_index_thus_far_delta = 0
        self.max_index_thus_far = 0
        self.n_cores = n_cores
        assert self.n_cores > 0
        self.parallelization_type = parallelization_type

        # if self.n_cores:
        #     apx_exact_24_manager = multiprocessing.Manager()

        #     self.dict_fxn_s_ib_single_i = apx_exact_24_manager.dict()
        #     self.dict_fxn_s_ib_single_i_apx = apx_exact_24_manager.dict()
        #     self.dict_fxn_demand_irf = apx_exact_24_manager.dict()
        #     self.dict_fxn_t_bar_min_irf = apx_exact_24_manager.dict()
        #     self.dict_fxn_demand_if = apx_exact_24_manager.dict()
        #     self.dict_fxn_t_bar_ma = apx_exact_24_manager.dict()
        #     self.dict_fxn_r_ij = apx_exact_24_manager.dict()
        #     self.dict_fxn_t_bar_min_index_link = apx_exact_24_manager.dict()
        #     self.dict_fxn_t_bar_min_index = apx_exact_24_manager.dict()
        #     self.dict_fxn_miat_t_i_b_single = apx_exact_24_manager.dict()
        #     self.dict_fxn_peak_speed_rpm_rpm = apx_exact_24_manager.dict()
        #     self.dict_fxn_t_bar_min_rpm = apx_exact_24_manager.dict()
        #     self.dict_fxn_t_p_min_rpm = apx_exact_24_manager.dict()
        #     self.dict_fxn_c = apx_exact_24_manager.dict()
        #     self.dict_fxn_s_ib_single_j_iterating = apx_exact_24_manager.dict()

        # else:

        self.dict_fxn_s_ib_single_i = None
        self.dict_fxn_s_ib_single_i_apx = None
        self.dict_fxn_demand_irf = None
        self.dict_fxn_t_bar_min_irf = None
        self.dict_fxn_demand_if = None
        self.dict_fxn_t_bar_ma = None
        self.dict_fxn_r_ij = None
        self.dict_fxn_t_bar_min_index_link = None
        self.dict_fxn_t_bar_min_index = None
        self.dict_fxn_miat_t_i_b_single = None
        self.dict_fxn_peak_speed_rpm_rpm = None
        self.dict_fxn_t_bar_min_rpm = None
        self.dict_fxn_t_p_min_rpm = None
        self.dict_fxn_c = None
        self.dict_fxn_s_ib_single_j_iterating = None

        self.dict_fxn_s_ib_single_i_local = dict()
        self.dict_fxn_s_ib_single_i_apx_local = dict()
        self.dict_fxn_demand_irf_local = dict()
        self.dict_fxn_t_bar_min_irf_local = dict()
        self.dict_fxn_demand_if_local = dict()
        self.dict_fxn_t_bar_ma_local = dict()
        self.dict_fxn_r_ij_local = dict()
        self.dict_fxn_t_bar_min_index_link_local = dict()
        self.dict_fxn_t_bar_min_index_local = dict()
        self.dict_fxn_miat_t_i_b_single_local = dict()
        self.dict_fxn_peak_speed_rpm_rpm_local = dict()
        self.dict_fxn_t_bar_min_rpm_local = dict()
        self.dict_fxn_t_p_min_rpm_local = dict()
        self.dict_fxn_c_local = dict()
        self.dict_fxn_s_ib_single_j_iterating_local = dict()

        self.counter_dict_fxn_s_ib_single_i = 0
        self.counter_dict_fxn_s_ib_single_i_memo = 0
        self.counter_dict_fxn_s_ib_single_i_apx = 0
        self.counter_dict_fxn_demand_irf = 0
        self.counter_dict_fxn_demand_if = 0
        self.counter_dict_fxn_r_ij = 0
        self.counter_dict_fxn_t_bar_min_index = 0
        self.counter_dict_fxn_miat_t_i_b_single = 0
        self.counter_dict_fxn_t_bar_min_rpm = 0
        self.counter_dict_fxn_c = 0
        self.counter_dict_fxn_s_ib_single_j_iterating = 0

        self.parallelized_deltas_start_time_s = 0
        self.parallelized_modes_start_time_s = 0

        #Dictionaries (for memoization)
        self.memoization = True

        self.k = -1

    def calculate_demand_seq(self,print_progress,delta_list,eff,apx):

        """ Calculate max demand in time \\delta using PDSs """

        #Hard Coded setup
        mode = 3
        use_irf_analytic_miat = mode & 0b001
        elimination = mode & 0b010

        #Results table
        delta_table = None

        if self.n_cores > 1:

            if self.parallelization_type == 0:

                (delta_table,delta_table_creation_time_s) = self.calculate_demand_seq_parallelize_deltas(use_irf_analytic_miat,elimination,print_progress,delta_list,eff,apx)

            else:

                (delta_table,delta_table_creation_time_s) = self.calculate_demand_seq_parallelize_modes(use_irf_analytic_miat,elimination,print_progress,delta_list,eff,apx)

        else:

            (delta_table,delta_table_creation_time_s) = self.calculate_demand_seq_uniprocessor(use_irf_analytic_miat,elimination,print_progress,delta_list,eff,apx)

        if print_progress >= 1:
            print("Gets/Total:", self.counter_dict_fxn_s_ib_single_i_memo,"/",self.counter_dict_fxn_s_ib_single_i)

        return (delta_table,delta_table_creation_time_s)

    def calculate_demand_seq_parallelize_deltas(self,use_irf_analytic_miat,elimination,print_progress,delta_list,eff,apx):

        """Calculate max demand in time \\delta using PDSes using parallelized subsets of delta list (# deltas/processors per processor)"""

        # self.print_output_signature(use_irf_analytic_miat,elimination,print_progress,eff,apx)

        self.parallelized_deltas_start_time_s = perf_counter()

        #Count number of intervals for dbf
        num_deltas = len(delta_list)

        #Build table for logging runtimes
        delta_table = [[-1 for i in range(4)] for j in range(num_deltas)]

        #Create results arrays
        process_results = [-1]*self.n_cores
        results_array = [-1]*self.n_cores
        cumulative_time_results = [-1]*self.n_cores

        #Create process pool
        pool = multiprocessing.Pool(processes=self.n_cores)

        #Find the maximum usable cores
        usable_cores_maximum = min(self.n_cores,len(delta_list))

        #Construct sub arrays
        sub_arrays = delta_mode_allocator.delta_allocator(delta_list,self.n_cores)

        #For every subarray...
        for i in range(usable_cores_maximum):

            #Parallelize
            process_results[i] = pool.apply_async(self.calculate_demand_seq_uniprocessor, args=(use_irf_analytic_miat,elimination,print_progress,sub_arrays[i],eff,apx))

        #For every process...
        for i in range(usable_cores_maximum):
            #Collect results
            (results_array[i],cumulative_time_results[i]) = process_results[i].get()

        #Close and join pool (shutdown parallelization)
        pool.close()
        pool.join()

        #For every result...
        for i in range(usable_cores_maximum):
            if i == 0:
                delta_table = results_array[i]
            else:
                delta_table += results_array[i]
        print(delta_table)
        delta_table = sorted(delta_table)

        parallelized_deltas_end_time_s = perf_counter()
        delta_table_creation_time_s = parallelized_deltas_end_time_s - self.parallelized_deltas_start_time_s

        self.fxn_reset_all_tables()

        return (delta_table,delta_table_creation_time_s)

    def calculate_demand_seq_parallelize_modes(self,use_irf_analytic_miat,elimination,print_progress,delta_list,eff,apx):

        """Calculate max demand in time \\delta using PDSes using parallelized modes over all deltas (# modes / processors per processor)"""

        # self.print_output_signature(use_irf_analytic_miat,elimination,print_progress,eff,apx)

        #Count number of intervals for dbf
        num_deltas = len(delta_list)

        #Build table for logging runtimes
        delta_table = [[-1 for i in range(4)] for j in range(num_deltas)]

        #Start time for entire "dbf"
        self.parallelized_modes_start_time_s = perf_counter()

        #Create results arrays
        process_results = [-1]*self.n_cores
        results_array = [-1]*self.n_cores

        #Create process pool
        pool = multiprocessing.Pool(processes=self.n_cores)

        #Find the maximum usable cores
        usable_cores_maximum = min(self.n_cores,self.t_avr.m)

        #Construct sub arrays
        sub_arrays = delta_mode_allocator.mode_allocator(self.t_avr.m,usable_cores_maximum)

        #For every mode...
        for i in range(usable_cores_maximum):

            #Parallelize
            process_results[i] = pool.apply_async(self.calculate_demand_seq_mode_list, args=(use_irf_analytic_miat,elimination,print_progress,delta_list,eff,apx,sub_arrays[i]))

        for i in range(usable_cores_maximum):
            #Collect results
            results_array[i] = process_results[i].get()

        pool.close()
        pool.join()

        for d in range(num_deltas):
            max_demand = 0
            max_demand_id = -1

            for i in range(usable_cores_maximum):

                if results_array[i][d][1] > max_demand:
                    max_demand_id = i
                    max_demand = results_array[i][d][1]

            delta_table[d] = results_array[max_demand_id][d]

        delta_table_creation_end_time_s = perf_counter()
        delta_table_creation_time_s = delta_table_creation_end_time_s - self.parallelized_modes_start_time_s

        #Calculate times for every \\delta
        #For every demand interval...
        for d in range(num_deltas):

            individual_time = 0     #Assume individual time is zero

            for i in range(usable_cores_maximum):   #For every processor...
                print("Core ",i," : ", results_array[i][d][2])
                individual_time = max(results_array[i][d][2],individual_time)  #Take the max individual time for this \\delta

            delta_table[d][2] = individual_time     #Assign individual demand interval processing time

            cumulative_time = 0

            for i in range(usable_cores_maximum):   #For every processor...
                cumulative_time = max(results_array[i][d][3],cumulative_time)

            #Mark cumulative as negative
            delta_table[d][3] = cumulative_time

        self.fxn_reset_all_tables()

        print(perf_counter()," - Returning results")
        return (delta_table,delta_table_creation_time_s)

    def calculate_demand_seq_mode_list(self,use_irf_analytic_miat,elimination,print_progress,delta_list,eff,apx,mode_list):

        """Calculate max demand for all \\delta starting at modes in mode_list using PDSes"""

        num_deltas = len(delta_list)
        num_modes = len(mode_list)

        delta_table = [[-1 for i in range(4)] for j in range(num_deltas)]

        for d in range(num_deltas):

            start_s = perf_counter()

            delta_us = delta_list[d]

            max_demand = 0
            max_pattern = (0,[0])

            for i in range(num_modes):

                (demand,pattern) = self.calculate_demand_seq_single_delta_single_mode(delta_us,use_irf_analytic_miat,elimination,print_progress,eff,apx,mode_list[i])

                if demand > max_demand:
                    max_demand = demand
                    max_pattern = pattern

            end_s = perf_counter()

            individual_delta_time_s = end_s - start_s
            cumulative_time_s = end_s - self.parallelized_modes_start_time_s

            delta_table[d][0] = delta_us
            delta_table[d][1] = max_demand
            delta_table[d][2] = individual_delta_time_s
            delta_table[d][3] = cumulative_time_s

            if print_progress >= 2:
                print_output = (str(d) + "," + str(max_demand)
                        + "," + str(max_pattern))
                print(print_output)

        self.fxn_reset_all_tables()

        return delta_table

    def calculate_demand_seq_single_delta_single_mode(self,delta_value,use_irf_analytic_miat,elimination,print_progress,eff,apx,mode):

        """Calculate max demand and sequence producing max demand over interval \\delta"""

        max_demand = 0
        b_safe_max = 0
        max_demand_miat = None
        max_demand_seq = None

        # delta_value = delta_list[delta_index]

        max_util = self.t_avr.get_max_mode_utilization()

        #Begin binary search for max b which with MIAT <= delta
        b_lo = 0
        if eff:
            b_hi = math.ceil(delta_value * max_util)
        else:
            b_hi = delta_value

        while b_lo <= b_hi:

            b_search = (b_hi + b_lo) // 2

            # print(delta_value,b_search)

            if apx:
                (miat,sln_seq,b_safe) = self.fxn_t_ib_apx_single_mode(mode,b_search,self.avr_apx,use_irf_analytic_miat,elimination)
            else:
                (miat,sln_seq) = self.fxn_t_ib_single_mode(mode,b_search,use_irf_analytic_miat,elimination)

            if(miat <= delta_value and b_search > max_demand):
                max_demand = b_search
                max_demand_seq = sln_seq
                max_demand_miat = miat
                if apx:
                    b_safe_max = b_safe

            max_is_higher = miat <= delta_value

            if max_is_higher:

                b_lo = b_search + 1

            else:

                b_hi = b_search - 1

        print_output = (str(delta_value) + ","
                        + str(max_demand_miat) + "," + str(max_demand)
                        + "," + str(max_demand_seq))

        if apx:
            print_output += "," + str(b_safe_max)

        if print_progress >= 1:
            print(print_output)

        if apx:
            return (b_safe_max,sln_seq)
        else:
            return (max_demand,sln_seq)

    def fxn_t_ib_single_mode(self,i,b,use_irf,eliminate_bad_solutions):

        """Get MIAT of all sequences beginning with \\omega_i and D(S)>=b"""

        if USE_ASSERTS:
            assert i >= 1
            assert i <= self.m
            assert b >= 0

            assert i % 1 == 0
            assert b % 1 == 0

        if b == 0:
            return (0,0)

        seq_set = self.fxn_s_ib_single_i(i,b,use_irf,eliminate_bad_solutions)

        seq_set_length = len(seq_set)

        if USE_ASSERTS:
            assert seq_set_length
            assert len(seq_set[0])
            if use_irf:
                assert len(seq_set[0][0]) == 3


        miat_min_array = [0]*seq_set_length

        for x in range(seq_set_length):

            if use_irf:
                seq_miat = self.fxn_t_bar_min_irf_arr(seq_set[x])
            else:
                seq_miat = self.fxn_miat_min(seq_set[x])
            miat_min_array[x] = seq_miat

        if not miat_min_array:

            miat_min = math.inf

        else:

            miat_min = min(miat_min_array)

        sln_index = miat_min_array.index(miat_min)
        sln_seq = seq_set[sln_index]

        miat_us = time_conversions.fxn_min_to_us(miat_min)

        return (miat_us,sln_seq)

    def fxn_t_ib_apx_single_mode(self,i,b,apx_instance,use_irf,eliminate_bad_solutions):

        """Get MIAT of all sequences beginning with \\omega_1 thru \\omega_m and D(S)>=b"""

        assert i >= 1
        assert i <= self.t_avr.m
        assert b >= 0

        assert i % 1 == 0
        assert b % 1 == 0

        if b == 0:
            return (0,0,0)

        #Extract e_b, approximate b
        e_b = apx_instance.epsilon_b
        self.fxn_create_k_apx(e_b,b)
        b_prime = math.floor(b/self.k)

        seq_set = self.fxn_s_ib_single_i_apx(i,b_prime,apx_instance,use_irf,eliminate_bad_solutions)

        seq_set_length = len(seq_set)
        assert seq_set_length
        assert len(seq_set[0])
        if use_irf:
            assert len(seq_set[0][0]) == 3


        miat_min_array = [0]*seq_set_length

        for x in range(seq_set_length):

            if use_irf:
                seq_miat = self.fxn_t_bar_min_irf_arr(seq_set[x])
            else:
                seq_miat = self.fxn_miat_min(seq_set[x])
            miat_min_array[x] = seq_miat

        if not miat_min_array:

            miat_min = math.inf

        else:

            miat_min = min(miat_min_array)

        sln_index = miat_min_array.index(miat_min)
        sln_seq = seq_set[sln_index]

        miat_us = time_conversions.fxn_min_to_us(miat_min)

        b_safe = self.k*b_prime /(apx_instance.one_minus_epsilon)

        self.fxn_reset_k_and_k_based_tables()

        return (miat_us,sln_seq,b_safe)

    def calculate_demand_seq_single_delta(self,delta_value,use_irf_analytic_miat,elimination,eff,apx):

        """Calculate max demand and sequence producing max demand over interval \\delta"""

        #Start timer
        start_s = perf_counter()

        max_demand = 0
        # max_demand_miat = 0
        # max_demand_seq = []
        if apx:
            b_safe_max = 0


        # delta_value = delta_list[delta_index]

        max_util = self.t_avr.get_max_mode_utilization()

        #Begin binary search for max b which with MIAT <= delta
        b_lo = 0
        if eff:
            b_hi = math.ceil(delta_value * max_util)
        else:
            b_hi = delta_value

        while b_lo <= b_hi:

            b_search = (b_hi + b_lo) // 2

            # print(delta_value,b_search)

            if apx:
                (miat,sln_seq,b_safe) = self.fxn_t_ib_apx(self.t_avr.m,b_search,self.avr_apx,use_irf_analytic_miat,elimination)
            else:
                (miat,sln_seq) = self.fxn_t_ib(self.t_avr.m,b_search,use_irf_analytic_miat,elimination)

            if(miat <= delta_value and b_search > max_demand):
                max_demand = b_search
                max_demand_seq = sln_seq
                max_demand_miat = miat
                if apx:
                    b_safe_max = b_safe

            max_is_higher = miat <= delta_value

            if max_is_higher:

                b_lo = b_search + 1

            else:

                b_hi = b_search - 1

        #Time stop
        end_s = perf_counter()


        individual_delta_time_s = end_s-start_s

        if apx:
            return (delta_value,b_safe_max,individual_delta_time_s)
        else:
            return (delta_value,max_demand,individual_delta_time_s)

    def calculate_demand_seq_uniprocessor(self,use_irf_analytic_miat,elimination,print_progress,delta_list,eff,apx):

        """Calculate max demand for all \\delta using PDSes and single processor (1 core 1 thread)"""

        #Count number of intervals for dbf
        num_deltas = len(delta_list)

        #Build table for logging runtimes
        delta_table = [[-1 for i in range(4)] for j in range(num_deltas)]

        #Start time for entire "dbf"
        delta_table_creation_time_start_s = perf_counter()

        for delta_index in range(num_deltas):

            delta_value = delta_list[delta_index]

            (delta_value,demand,individual_delta_time) = self.calculate_demand_seq_single_delta(delta_value,use_irf_analytic_miat,elimination,eff,apx)

            delta_table[delta_index][0] = delta_value
            delta_table[delta_index][1] = demand
            delta_table[delta_index][2] = individual_delta_time
            cumulative_time = perf_counter() - delta_table_creation_time_start_s
            delta_table[delta_index][3] = cumulative_time

            # if self.n_cores and delta_index % 5 == 0:
            #     self.memoization_sync()

        delta_table_creation_time_end_s = perf_counter()
        delta_table_creation_time_s = delta_table_creation_time_end_s - delta_table_creation_time_start_s

        self.fxn_reset_all_tables()

        return (delta_table,delta_table_creation_time_s)

    def fxn_t_ib(self,i,b,use_irf,eliminate_bad_solutions):

        """Get MIAT of all sequences beginning with \\omega_1 thru \\omega_m and D(S)>=b"""

        if USE_ASSERTS:
            assert i >= 1
            assert i <= self.m
            assert b >= 0

            assert i % 1 == 0
            assert b % 1 == 0

        if b == 0:
            return (0,0)

        seq_set = self.fxn_s_ib(i,b,use_irf,eliminate_bad_solutions)

        seq_set_length = len(seq_set)

        if USE_ASSERTS:
            assert seq_set_length
            assert len(seq_set[0])
            if use_irf:
                assert len(seq_set[0][0]) == 3


        miat_min_array = [0]*seq_set_length

        for x in range(seq_set_length):

            if use_irf:
                seq_miat = self.fxn_t_bar_min_irf_arr(seq_set[x])
            else:
                seq_miat = self.fxn_miat_min(seq_set[x])
            miat_min_array[x] = seq_miat

        if not miat_min_array:

            miat_min = math.inf

        else:

            miat_min = min(miat_min_array)

        sln_index = miat_min_array.index(miat_min)
        sln_seq = seq_set[sln_index]

        miat_us = time_conversions.fxn_min_to_us(miat_min)

        return (miat_us,sln_seq)

    def fxn_s_ib(self,i,b,use_irf,eliminate_bad_solutions):

        """Get all sequences beginning with \\omega_1 thru \\omega_m and D(S)>=b"""

        if USE_ASSERTS:

            assert i >= 1
            assert i <= self.m
            assert b >= 0

            assert i % 1 == 0
            assert b % 1 == 0

        seq_set_i_b = []

        if b > 0:

            for x in range(1,i+1):
                seq_set_i_b_single = self.fxn_s_ib_single_i(x,b,use_irf,eliminate_bad_solutions)
                seq_set_i_b += seq_set_i_b_single

        return seq_set_i_b

    def fxn_t_bar_min_irf_arr(self,irf_arr):

        """MIAT (in minutes) for S_i^rf"""

        if USE_ASSERTS:
            irf_arr_len = len(irf_arr)
            assert irf_arr_len
            assert len(irf_arr[0]) == 3

        miat_min = self.fxn_t_irf_arr(irf_arr)

        return miat_min

    def fxn_miat_min(self,seq):

        """Get MIAT of sequence seq in min"""

        alpha = self.t_avr.alpha

        l = len(seq)

        if l == 0:
            return 0

        miat_sum_minutes = 0

        for i in range(l-1):

            s_1 = seq[i]
            s_2 = seq[i+1]
            t_bar_min_rpm_val = self.fxn_t_bar_min_rpm(s_1,s_2)
            miat_sum_minutes += t_bar_min_rpm_val

        s_n = seq[l-1]
        t_bar_min_rpm_final_val = self.fxn_t_bar_min_rpm(s_n,math.sqrt(s_n**2+2*alpha))
        miat_sum_minutes += t_bar_min_rpm_final_val

        return miat_sum_minutes

    def fxn_s_ib_single_i(self,i,b,use_irf,eliminate_bad_solutions):

        """Get the set of seq with s_1 = \\omega_i, D(S) >= b"""

        self.counter_dict_fxn_s_ib_single_i += 1

        if USE_ASSERTS:

            assert i >= 1
            assert i <= self.m

            assert i % 1 == 0
            assert b % 1 == 0

        if b <= 0:

            return []

        if self.memoization:
            ans = self.memoization_get(self.dict_fxn_s_ib_single_i_local,self.dict_fxn_s_ib_single_i,(i,b))
            if ans is not None:
                self.counter_dict_fxn_s_ib_single_i_memo += 1
                return ans

        seq_set_i_b_single_f_iterating = self.fxn_s_ib_single_f_iterating(i,b,use_irf,eliminate_bad_solutions)
        seq_set_i_b_single_j_iterating = self.fxn_s_ib_single_j_iterating(i,b,use_irf,eliminate_bad_solutions)

        output = seq_set_i_b_single_f_iterating + seq_set_i_b_single_j_iterating

        if eliminate_bad_solutions:
            output_actual = self.fxn_eliminate_bad_solutions(output,use_irf)
        else:
            output_actual = output

        if self.memoization :
            self.memoization_set(self.dict_fxn_s_ib_single_i_local,self.dict_fxn_s_ib_single_i,(i,b),output_actual)

        return output_actual

    def fxn_t_irf_arr(self,irf_arr):

        """Get MIAT for S_{i}^{r,f} array"""

        q = len(irf_arr)

        assert q > 0

        if q == 1:

            i = irf_arr[0][0]
            r = irf_arr[0][1]
            f = irf_arr[0][2]

            t_irf = self.fxn_t_irf(i,r,f)
            t_f_irf = self.fxn_t_f_irf(i,r,f)

            miat_minutes = t_irf + t_f_irf

        if q > 1:

            miat_minutes = 0

            for x in range(q-1):

                i = irf_arr[x][0]
                r = irf_arr[x][1]
                f = irf_arr[x][2]
                j = irf_arr[x+1][0]

                t_irf = self.fxn_t_irf(i,r,f)
                t_l_irfj = self.fxn_t_l_irfj(i,r,f,j)

                miat_local_minutes = t_irf + t_l_irfj

                miat_minutes += miat_local_minutes

            i_q = irf_arr[q-1][0]
            r_q = irf_arr[q-1][1]
            f_q = irf_arr[q-1][2]

            t_irf = self.fxn_t_irf(i_q,r_q,f_q)
            t_f_irf = self.fxn_t_f_irf(i_q,r_q,f_q)

            miat_minutes += t_irf + t_f_irf

        return miat_minutes

    def fxn_t_bar_min_rpm(self,omega_i,omega_j):

        """MIAT (in minutes) from \\omega_i to \\omega_j in minutes - honor peak limit"""

        omega_m = self.t_avr.omega[-1]

        omega_i = min(omega_i,omega_m)
        omega_j = min(omega_j,omega_m)

        if self.memoization:
            ans = self.memoization_get(self.dict_fxn_t_bar_min_rpm_local,self.dict_fxn_t_bar_min_rpm,(omega_i,omega_j))
            if ans is not None:
                return ans

        if USE_OMEGA_ASSERTS:
            assert not self.fxn_assert_omega_rpms(omega_i,omega_j)

        miat_minutes = self.t_avr.fxn_t_bar_min_rpm(omega_i,omega_j)

        if self.memoization:
            self.memoization_set(self.dict_fxn_t_bar_min_rpm_local,self.dict_fxn_t_bar_min_rpm,(omega_i,omega_j),miat_minutes)

        return miat_minutes

    def fxn_s_ib_single_f_iterating(self,i,b,use_irf,eliminate_bad_solutions):

        """Find a sequence with minimum interarrival time which begins with speed \\omega_i,
        is NOT composed of a subsequence starting at another boundary speed, and generates demand b"""

        output = []

        c_m = self.t_avr.wcet[-1]

        f_max_by_r_im = self.fxn_r(i,self.t_avr.m)
        f_max_by_wcet = math.ceil(b/c_m)
        max_f = min(f_max_by_wcet, f_max_by_r_im)

        for f in range(0,max_f+1):

            seq_irf_f_only = self.fxn_create_speed_seq(i,0,f,use_irf)

            d_f = self.fxn_demand(seq_irf_f_only,use_irf)

            d_remaining = b - d_f

            if d_remaining > 0:

                c_i = self.t_avr.wcet[i]

                r_min = math.ceil(d_remaining/c_i)

                seq_proposed = self.fxn_create_speed_seq(i,r_min,f,use_irf)

                d_seq_proposed = self.fxn_demand(seq_proposed,use_irf)

                if USE_ASSERTS:
                    assert d_seq_proposed >= b
                    assert d_seq_proposed - c_i < b

                seq_irf = seq_proposed

            else:

                seq_irf = seq_irf_f_only

            if use_irf:
                output += [[seq_irf]]
            else:
                output += [seq_irf]

        if eliminate_bad_solutions:
            output_actual = self.fxn_eliminate_bad_solutions(output,use_irf)
        else:
            output_actual = output

        return output_actual

    def fxn_s_ib_single_j_iterating(self,i,b,use_irf,eliminate_bad_solutions):

        """Find a sequence with minimum interarrival time which begins with speed \\omega_i,
        IS composed of a subsequence starting at another boundary speed, and generates demand b"""

        if self.memoization:
            ans = self.memoization_get(self.dict_fxn_s_ib_single_j_iterating_local,self.dict_fxn_s_ib_single_j_iterating,(i,b))
            if ans is not None:
                return ans

        output = []

        c_i = self.t_avr.wcet[i]

        for j in range(i+1,self.t_avr.m+1):

            f_i_to_j = self.fxn_r(i,j)

            seq_f_i_to_j_only = self.fxn_create_speed_seq(i,0,f_i_to_j,use_irf)

            d_f_i_to_j_only = self.fxn_demand(seq_f_i_to_j_only,use_irf)

            d_remaining_for_r = b - d_f_i_to_j_only

            r_max = math.ceil(d_remaining_for_r/c_i)

            for r in range(0,r_max+1):

                omega_r_rij = self.fxn_create_speed_seq(i,r,f_i_to_j,use_irf)

                d_omega_r_rij = self.fxn_demand(omega_r_rij,use_irf)

                d_remaining_for_s_ib = b - d_omega_r_rij

                seq_set_i_single_remaining = self.fxn_s_ib_single_i(j,d_remaining_for_s_ib,use_irf,eliminate_bad_solutions)

                for seq_remain in seq_set_i_single_remaining:

                    if use_irf:
                        assert omega_r_rij[0] != seq_remain[0][0]
                        output += [[omega_r_rij] + seq_remain]
                    else:
                        output += [omega_r_rij + seq_remain]

        if eliminate_bad_solutions:
            output_actual = self.fxn_eliminate_bad_solutions(output,use_irf)
        else:
            output_actual = output

        if self.memoization:

            self.memoization_set(self.dict_fxn_s_ib_single_j_iterating_local,self.dict_fxn_s_ib_single_j_iterating,(i,b),output_actual)

        return output_actual

    def fxn_eliminate_bad_solutions(self,input_seqs,use_irf):

        """Given a list of candidate speed sequences, return only the seq with min interarrival time"""

        if input_seqs == []:
            return []

        #Output Processing
        output_miat_only = []

        if use_irf:
            miat_array = list(map(self.fxn_t_bar_min_irf_arr,input_seqs))
        else:
            miat_array = list(map(self.fxn_miat_min,input_seqs))

        miat = min(miat_array)
        output_index_with_miat = miat_array.index(miat)

        output_miat_only = [input_seqs[output_index_with_miat]]

        output_actual = output_miat_only

        return output_actual

    def fxn_t_irf(self,i,r,f):

        """Get MIAT of \\Omega_{i}^{r,f}"""

        t_rb = self.fxn_t_rb_ir(i,r)
        t_l_rm = self.fxn_t_rm_irf(i,r,f)
        t_ma = self.fxn_t_ma_if(i,f)

        miat_minutes = t_rb + t_l_rm + t_ma

        return miat_minutes

    def fxn_t_f_irf(self,i,r,f):

        """Get MIAT for last job release at speed s_n \\in \\Omega_i^{r,f}"""

        s_1 = self.fxn_s_n_in_omega_irf(i,r,f)
        alpha = self.t_avr.alpha
        s_2 = math.sqrt(s_1**2+2*alpha)

        t_bar_s1_s2 = self.fxn_t_bar_min_rpm(s_1,s_2)

        miat_minutes = t_bar_s1_s2

        return miat_minutes

    def fxn_t_l_irfj(self,i,r_i,f_i,j):

        """Get MIAT between s_n of \\Omega_{i}^{r_i,f_i} and \\Omega_{j}^{r_j,f_j}"""

        omega_j = self.t_avr.omega[j]

        s_1 = self.fxn_s_n_in_omega_irf(i,r_i,f_i)
        s_2 = omega_j

        miat_minutes = self.fxn_t_bar_min_rpm(s_1,s_2)

        return miat_minutes

    def fxn_t_min_rpm(self,omega_i,omega_j):

        """Get MIAT from \\omega_i to \\omega_j in minutes -- without a maximum speed restriction"""

        if USE_OMEGA_ASSERTS:
            assert not self.fxn_assert_omega_rpms(omega_i,omega_j)

        return self.t_avr.fxn_t_min_rpm(omega_i,omega_j)

    def fxn_t_p_min_rpm(self,omega_i,omega_j):

        """MIAT in minutes when accelerating from
            \\omega_i to \\omega_j by rpm w/o exceeding \\omega_p"""

        if USE_OMEGA_ASSERTS:
            assert not self.fxn_assert_omega_rpms(omega_i,omega_j)

        if self.memoization:
            ans = self.memoization_get(self.dict_fxn_t_p_min_rpm_local,self.dict_fxn_t_p_min_rpm,(omega_i,omega_j))
            if ans is not None:
                return ans

        min_interarrival_time_minutes = self.t_avr.fxn_t_p_min_rpm(omega_i,omega_j)

        if self.memoization:
            self.memoization_set(self.dict_fxn_t_p_min_rpm_local,self.dict_fxn_t_p_min_rpm,(omega_i,omega_j),min_interarrival_time_minutes)

        return min_interarrival_time_minutes

    def fxn_r(self,i,j):

        """Get # releases between \\omega_i and \\omega_j"""

        if USE_OMEGA_ASSERTS:
            assert not self.fxn_assert_omega_indices(i,j)

        if self.memoization:
            ans = self.memoization_get(self.dict_fxn_r_ij_local,self.dict_fxn_r_ij,(i,j))
            if ans is not None:
                return ans

        if 0 < i < j:

            theta = self.fxn_theta(i,j)

            output = math.ceil(theta)

        else:

            output = 0

        if self.memoization:
            self.memoization_set(self.dict_fxn_r_ij_local,self.dict_fxn_r_ij,(i,j),output)

        return output

    def fxn_create_speed_seq(self,i,r,f,use_irf):

        """Create speed sequence in truncated or expanded form"""

        if use_irf: #Truncated
            seq = [i,r,f]
        else: #Expanded
            seq = self.fxn_omega_irf(i,r,f)

        return seq

    def fxn_demand(self,seq,use_irf):

        """Get sequence demand"""

        if use_irf:

            return self.fxn_demand_irf(seq)

        else:

            return self.fxn_demand_rpm_seq(seq)

    def fxn_t_rb_ir(self,i,r):

        """Get MIAT for RB sequence"""

        if r > 0:

            t_bar_i_to_i = self.fxn_t_bar_min_index(i,i)

            miat_minutes = (r-1) * t_bar_i_to_i

        else:

            miat_minutes = 0

        return miat_minutes

    def fxn_t_rm_irf(self,i,r,f):

        """Get MIAT for s_n \\in RB(i,r) to s_1 \\in MA(i,f)"""

        if r > 0 and f > 0:

            miat_minutes = self.fxn_t_bar_min_index(i,i)

        else:

            miat_minutes = 0

        return miat_minutes

    def fxn_t_ma_if(self,i,f):

        """Get MIAT of MA(i,f)"""

        if f > 0:

            omega_i = self.t_avr.omega[i]
            alpha = self.t_avr.alpha

            miat_minutes = (math.sqrt(omega_i**2 + 2*alpha*(f-1)) - omega_i)/alpha

        else:

            miat_minutes = 0

        return miat_minutes

    def fxn_s_n_in_omega_irf(self,i,r,f):

        """Get s_n \\in \\omega_i^{rf}"""

        if r == 0 and f == 0:

            output = None

        elif r > 0 and f == 0:

            output = self.t_avr.omega[i]

        elif f > 0:

            output = math.sqrt(self.t_avr.omega[i]**2+2*self.t_avr.alpha*(f-1))

        else:

            assert 0

        return output

    def fxn_theta(self,i,j):

        """Get distance (# releases) from \\omega_i to \\omega_j"""

        if USE_OMEGA_ASSERTS:
            assert not self.fxn_assert_omega_indices(i,j)

        alpha = self.t_avr.alpha
        omega_i = self.t_avr.omega[i]
        omega_j = self.t_avr.omega[j]

        distance = (omega_j**2 - omega_i**2)/(2*alpha)

        return distance

    def fxn_omega_irf(self,i,r,f):

        """Create RB-MA sequence"""

        assert i >= 1
        assert i <= self.t_avr.m
        assert r >= 0
        assert f >= 0

        assert i % 1 == 0
        assert r % 1 == 0
        assert f % 1 == 0

        rb_seq = self.fxn_omega_rb(i,r)

        ma_seq = self.fxn_omega_ma(i,f)

        rbma_seq = rb_seq + ma_seq

        return rbma_seq

    def fxn_demand_irf(self,sub_seq_irf):

        """Get demand of dominant sequence"""

        # assert len(sub_seq_irf) == 3

        if self.memoization:

            i = sub_seq_irf[0]
            r = sub_seq_irf[1]
            f = sub_seq_irf[2]

            # if self.n_cores:
            #     lock_dict_fxn_demand_irf.acquire()
            ans = self.memoization_get(self.dict_fxn_demand_irf_local,self.dict_fxn_demand_irf,(i,r,f))
            if ans is not None:
                return ans

        demand_sum_us = 0

        demand_sum_us = self.fxn_d_irf(sub_seq_irf)

        if self.memoization:
            self.memoization_set(self.dict_fxn_demand_irf_local,self.dict_fxn_demand_irf_local,(i,r,f),demand_sum_us)

        return demand_sum_us

    def fxn_demand_rpm_seq(self,seq):

        """Get demand of speed sequence"""

        if len(seq) == 0:
            return 0

        demand_sum_us = 0

        for s in seq:

            demand_sum_us += self.fxn_c(s)

        return demand_sum_us

    def fxn_t_bar_min_index(self,i,j):

        """MIAT (in minutes) from \\omega_i to \\omega_j in minutes - honor peak limit"""

        if USE_OMEGA_ASSERTS:
            assert not self.fxn_assert_omega_indices(i,j)

        if self.memoization:
            ans = self.memoization_get(self.dict_fxn_t_bar_min_index_local,self.dict_fxn_t_bar_min_index,(i,j))
            if ans is not None:
                return ans

        omega_i = self.t_avr.omega[i]
        omega_j = self.t_avr.omega[j]

        miat_minutes = self.fxn_t_bar_min_rpm(omega_i,omega_j)

        if self.memoization:
            self.memoization_set(self.dict_fxn_t_bar_min_index_local,self.dict_fxn_t_bar_min_index,(i,j),miat_minutes)

        return miat_minutes

    def fxn_omega_rb(self,i,r):

        """Create RB sequence"""

        assert i >= 1
        assert i <= self.t_avr.m
        assert r >= 0

        assert i % 1 == 0
        assert r % 1 == 0

        rb_seq = [self.t_avr.omega[i]]*r

        return rb_seq

    def fxn_omega_ma(self,i,f):

        """Create MA sequence"""

        assert i >= 1
        assert i <= self.t_avr.m
        assert f >= 0

        assert i % 1 == 0
        assert f % 1 == 0

        ma_seq = []

        if f == 0:

            pass

        elif f > 0 and 1 <= i <= self.t_avr.m:

            omega_i = self.t_avr.omega[i]
            alpha = self.t_avr.alpha

            r_im = self.fxn_r(i,self.t_avr.m)
            f_im_max = r_im

            #Subtract 1 from reps to account for k=0 counting towards the # reps
            reps = min(f,f_im_max)

            for k in range(1,reps+1):

                ma_seq+=[math.sqrt(omega_i**2+2*alpha*(k-1))]

        return ma_seq


    def fxn_d_irf(self,irf):

        """Demand (in us) for \\Omega_i^rf"""

        if USE_ASSERTS:
            assert len(irf) == 3

        i = irf[0]
        r = irf[1]
        f = irf[2]


        if USE_ASSERTS:
            assert i >= 1
            assert i <= self.m
            assert r >= 0
            assert f >= 0

            assert i % 1 == 0
            assert r % 1 == 0
            assert f % 1 == 0

        d_rb_ir = self.fxn_d_rb(i,r)
        d_ma_if = self.fxn_d_ma(i,f)

        d_us = d_rb_ir + d_ma_if

        return d_us

    def fxn_c(self,s):
        """Get WCET from speed."""

        assert s >= self.t_avr.omega[0]
        assert s <= self.t_avr.omega[-1]

        if self.memoization:
            ans = self.memoization_get(self.dict_fxn_c_local,self.dict_fxn_c,s)
            if ans is not None:
                return ans

        wcet = self.fxn_c_linear(s)

        if self.memoization:
            self.memoization_set(self.dict_fxn_c_local,self.dict_fxn_c,s,wcet)

        return wcet

    def fxn_d_rb(self,i,r):

        """Demand (in us) for RB(i,r)"""

        if USE_ASSERTS:

            assert i >= 1
            assert i <= self.m
            assert r >= 0

            assert i % 1 == 0
            assert r % 1 == 0

        c_i = self.t_avr.wcet[i]

        d_us = c_i * r

        return d_us

    def fxn_d_ma(self,i,f):

        """Demand (in us) for MA(i,f)"""

        if USE_ASSERTS:

            assert i >= 1
            assert i <= self.m
            assert f >= 0

            assert i % 1 == 0
            assert f % 1 == 0

        d_us = 0

        if f > 0:

            if self.memoization:
                ans = self.memoization_get(self.dict_fxn_demand_if_local,self.dict_fxn_demand_if,(i,f))
                if ans is not None:
                    return ans

            seq_ma = self.fxn_omega_ma(i,f)
            d_us = self.fxn_demand(seq_ma,False)

            if self.memoization:
                self.memoization_set(self.dict_fxn_demand_if_local,self.dict_fxn_demand_if,(i,f),d_us)

        return d_us

    def fxn_c_binary(self,s):
        """Get WCET from speed via binary search."""

        assert s >= self.t_avr.wcet[0]
        assert s <= self.t_avr.wcet[-1]
        i_lo = 1
        i_hi = self.t_avr.m

        while i_lo <= i_hi:

            mid = (i_hi + i_lo) // 2

            omega_lo = self.t_avr.omega[mid-1]
            omega_hi = self.t_avr.omega[mid]

            if s > omega_hi:

                i_lo = mid+1

            elif omega_lo < s <= omega_hi:

                return self.t_avr.wcet[mid]

            else:

                i_hi = mid-1

        assert False

    def fxn_c_linear(self,s):
        """Get WCET from speed via linear search."""

        assert s >= self.t_avr.omega[0]
        assert s <= self.t_avr.omega[-1]

        for i in range(self.t_avr.m):
            current_boundary = self.t_avr.omega[i+1]
            if s <= current_boundary:
                return self.t_avr.wcet[i+1]

    def fxn_t_ib_apx(self,i,b,apx_instance,use_irf,eliminate_bad_solutions):

        """Get MIAT of all sequences beginning with \\omega_1 thru \\omega_m and D(S)>=b"""

        assert i >= 1
        assert i <= self.t_avr.m
        assert b >= 0

        assert i % 1 == 0
        assert b % 1 == 0

        if b == 0:
            return (0,0,0)

        #Extract e_b, approximate b
        e_b = apx_instance.epsilon_b
        self.fxn_create_k_apx(e_b,b)
        b_prime = math.floor(b/self.k)

        seq_set = self.fxn_s_ib_apx(i,b_prime,apx_instance,use_irf,eliminate_bad_solutions)

        seq_set_length = len(seq_set)
        assert seq_set_length
        assert len(seq_set[0])
        if use_irf:
            assert len(seq_set[0][0]) == 3


        miat_min_array = [0]*seq_set_length

        for x in range(seq_set_length):

            if use_irf:
                seq_miat = self.fxn_t_bar_min_irf_arr(seq_set[x])
            else:
                seq_miat = self.fxn_miat_min(seq_set[x])
            miat_min_array[x] = seq_miat

        if not miat_min_array:

            miat_min = math.inf

        else:

            miat_min = min(miat_min_array)

        sln_index = miat_min_array.index(miat_min)
        sln_seq = seq_set[sln_index]

        miat_us = time_conversions.fxn_min_to_us(miat_min)

        b_safe = self.k*b_prime /(apx_instance.one_minus_epsilon)

        self.fxn_reset_k_and_k_based_tables()

        return (miat_us,sln_seq,b_safe)

    def fxn_create_k_apx(self,e_b,b):

        """Get K scalar for approximation of b"""

        assert b >= 0
        assert e_b > 0
        assert e_b < 1

        assert b % 1 == 0

        self.k =  e_b * b / self.t_avr.m

    def fxn_s_ib_apx(self,i,b,apx_instance,use_irf,eliminate_bad_solutions):

        """Get all sequences beginning with \\omega_1 thru \\omega_m and D(S)>=b"""

        assert i >= 1
        assert i <= self.t_avr.m
        assert b >= 0

        assert i % 1 == 0
        assert b % 1 == 0

        seq_set_i_b = []

        if b > 0:

            for x in range(1,i+1):

                seq_set_i_b_single = self.fxn_s_ib_single_i_apx(x,b,apx_instance,use_irf,eliminate_bad_solutions)
                seq_set_i_b += seq_set_i_b_single

        return seq_set_i_b

    def fxn_reset_k_and_k_based_tables(self):

        """Clear k-dependent hash tables"""

        self.k = -1

        self.dict_fxn_s_ib_single_i_apx_local.clear()

    def fxn_s_ib_single_i_apx(self,i,b,apx_instance,use_irf,eliminate_bad_solutions):

        """Get the set of seq with s_1 = \\omega_i, D(S) >= b"""

        assert i >= 1
        assert i <= self.t_avr.m

        assert i % 1 == 0
        assert b % 1 == 0

        if b <= 0:

            return []

        if self.memoization and b > 0:
            ans = self.memoization_get(self.dict_fxn_s_ib_single_i_apx_local,self.dict_fxn_s_ib_single_i_apx,(i,b))
            if ans is not None:
                self.counter_dict_fxn_s_ib_single_i_memo += 1
                return ans

        #Deconstruct APX
        e_r = apx_instance.epsilon_r
        e_f = apx_instance.epsilon_f

        seq_set_i_b_single = []
        seq_set_i_single_remaining = []

        if i == self.t_avr.m:

            c_i = self.t_avr.wcet[i]

            b_inflated = b + 1

            b_adjusted = math.ceil(b_inflated * self.k)

            r_min = math.ceil(b_adjusted/c_i)

            seq_proposed = self.fxn_create_speed_seq(i,r_min,0,use_irf)

            d_seq_proposed = self.fxn_demand_apx(seq_proposed,use_irf)

            assert d_seq_proposed >= b or r_min == 1
            assert d_seq_proposed - c_i < b or r_min == 1

            if use_irf:
                output = [[seq_proposed]]
            else:
                output = [seq_proposed]

        else: #i < self.t_avr.m:

            #Single boundary speed solutions

            f_p = self.fxn_set_f_prime(b,e_f)

            for f in f_p:

                seq_irf_f_only = self.fxn_create_speed_seq(i,0,f,use_irf)

                d_f = self.fxn_demand_apx(seq_irf_f_only,use_irf)

                b_inflated = b + 1
                b_adjusted = math.ceil(b_inflated * self.k)
                d_r_min = b_adjusted - d_f

                if d_r_min > 0:

                    c_i = self.t_avr.wcet[i]

                    r_min = math.ceil(d_r_min/c_i)

                    seq_proposed = self.fxn_create_speed_seq(i,r_min,f,use_irf)

                    d_seq_proposed = self.fxn_demand_apx(seq_proposed,use_irf)

                    assert d_seq_proposed >= b

                    seq_irf = seq_proposed

                else:

                    seq_irf = seq_irf_f_only

                if use_irf:
                    seq_set_i_b_single += [[seq_irf]]
                else:
                    seq_set_i_b_single += [seq_irf]

            #Multiple boundary speed solutions
            r_p = self.fxn_set_r_prime(b,i,e_r)

            for r in r_p:

                for j in range(i+1,self.t_avr.m+1):

                    r_ij = self.fxn_r(i,j)
                    f_i_to_j = r_ij

                    omega_r_rij = self.fxn_create_speed_seq(i,r,f_i_to_j,use_irf)

                    d_omega_r_rij = self.fxn_demand_apx(omega_r_rij,use_irf)

                    b_r = b - d_omega_r_rij

                    seq_set_i_single_remaining = self.fxn_s_ib_single_i_apx(j,b_r,apx_instance,use_irf,eliminate_bad_solutions)

                    for seq_remain in seq_set_i_single_remaining:

                        if use_irf:
                            assert omega_r_rij[0] != seq_remain[0][0]
                            seq_set_i_b_single += [[omega_r_rij] + seq_remain]
                        else:
                            seq_set_i_b_single += [omega_r_rij + seq_remain]

            output = seq_set_i_b_single

        if eliminate_bad_solutions:
            #Output Processing
            output_miat_only = []

            n_sequences = len(output)

            if n_sequences > 0:

                miat_array = [math.inf]*n_sequences

                for x in range(n_sequences):

                    if use_irf:
                        miat_array[x] = self.fxn_t_bar_min_irf_arr(output[x])
                    else:
                        miat_array[x] = self.fxn_miat_min(output[x])

                miat = min(miat_array)
                output_index_with_miat = miat_array.index(miat)

                output_miat_only = [output[output_index_with_miat]]

            output_actual = output_miat_only

        else:

            output_actual = output

        if self.memoization and b > 0:
            self.memoization_set(self.dict_fxn_s_ib_single_i_apx_local,self.dict_fxn_s_ib_single_i_apx,(i,b),output_actual)

        return output_actual

    def fxn_demand_apx(self,seq,use_irf):

        """Get approximate demand after scalar K division"""

        assert self.k != -1

        d = self.fxn_demand(seq,use_irf)

        d_apx = math.floor(d/self.k)

        return d_apx

    def fxn_set_f_prime(self,b,e_f):

        """Get approximated set of values for f"""

        assert b >= 0
        assert e_f > 0
        assert e_f < 1

        assert b % 1 == 0

        f_p = []

        c_m = self.t_avr.wcet[-1]

        ell_f = -math.log(math.ceil(b/c_m)) / math.log(1-e_f)

        for k in range(0,math.floor(ell_f)+1+1):

            apx_value = self.fxn_log_apx(b,c_m,e_f,k)

            f_p += [apx_value]

        return f_p

    def fxn_set_r_prime(self,b,i,e_r):

        """Get approximated set of values for r"""

        assert i >= 1
        assert i <= self.t_avr.m
        assert b >= 0
        assert e_r > 0
        assert e_r < 1

        assert i % 1 == 0
        assert b % 1 == 0

        r_p = []

        c_i = self.t_avr.wcet[i]

        ell_r = -math.log(math.ceil(b/c_i)) / math.log(1-e_r)

        for k in range(0,math.floor(ell_r)+1+1):

            apx_value = self.fxn_log_apx(b,c_i,e_r,k)

            r_p += [apx_value]

        return r_p

    def fxn_log_apx(self,b,c,e_x,k):

        """Get log approximation # of reps given values b, c, \\epsilon_x, and k"""

        assert c >= 1
        assert c <= self.t_avr.wcet[1]
        assert c >= self.t_avr.wcet[-1]
        assert b >= 0
        assert k >= 0
        assert e_x > 0
        assert e_x < 1

        assert b % 1 == 0
        assert c % 1 == 0
        assert k % 1 == 0

        ceil_part = math.ceil(b/c)
        epsilon_part = (1-e_x)**k

        output = math.floor(ceil_part * epsilon_part)

        return output

    def fxn_assert_omega_indices(self,i,j):

        """Assert expectations for \\Omega indices i and j"""

        assert i<=j
        assert i>0
        assert j>0
        assert i <= self.t_avr.m
        assert j <= self.t_avr.m
        assert i%1==0
        assert j%1==0

        return 0

    def fxn_assert_omega_rpms(self,omega_i,omega_j):

        """Assert expectations for speeds \\omega_i and \\omega_j"""

        assert omega_i >= self.t_avr.omega[0]
        assert omega_j >= self.t_avr.omega[0]

        assert omega_i <= self.t_avr.omega[-1]
        assert omega_j <= self.t_avr.omega[-1]

        return 0

    def fxn_reset_all_tables(self):

        """Clear all hash tables"""

        self.dict_fxn_c_local.clear()
        self.dict_fxn_s_ib_single_i_local.clear()
        self.dict_fxn_s_ib_single_i_apx_local.clear()
        self.dict_fxn_demand_irf_local.clear()
        self.dict_fxn_t_bar_min_irf_local.clear()
        self.dict_fxn_demand_if_local.clear()
        self.dict_fxn_t_bar_ma_local.clear()
        self.dict_fxn_r_ij_local.clear()
        self.dict_fxn_t_bar_min_index_link_local.clear()
        self.dict_fxn_t_bar_min_index_local.clear()
        self.dict_fxn_miat_t_i_b_single_local.clear()

    def memoization_get(self,dict_local,dict_shared,key):

        """Get memoized value if possible"""

        ans = dict_local.get(key)
        if ans is not None:
            return ans
        # elif self.n_cores and (ans := dict_shared.get(key)) is not None:
        #     return ans
        return None

    def memoization_set(self,dict_local,dict_shared,key,value):

        """Memoize value"""

        dict_local[key] = value

        # if self.n_cores:
        #     dict_shared[key] = value

    def memoization_sync(self):

        """Push local dict to shared, pull shared dicts to local"""

        #Push
        self.dict_fxn_s_ib_single_i.update(self.dict_fxn_s_ib_single_i_local)
        self.dict_fxn_s_ib_single_i_apx.update(self.dict_fxn_s_ib_single_i_apx_local)
        self.dict_fxn_demand_irf.update(self.dict_fxn_demand_irf_local)
        self.dict_fxn_t_bar_min_irf.update(self.dict_fxn_t_bar_min_irf_local)
        self.dict_fxn_demand_if.update(self.dict_fxn_demand_if_local)
        self.dict_fxn_t_bar_ma.update(self.dict_fxn_t_bar_ma_local)
        self.dict_fxn_r_ij.update(self.dict_fxn_r_ij_local)
        self.dict_fxn_t_bar_min_index_link.update(self.dict_fxn_t_bar_min_index_link_local)
        self.dict_fxn_t_bar_min_index.update(self.dict_fxn_t_bar_min_index_local)
        self.dict_fxn_miat_t_i_b_single.update(self.dict_fxn_miat_t_i_b_single_local)
        self.dict_fxn_peak_speed_rpm_rpm.update(self.dict_fxn_peak_speed_rpm_rpm_local)
        self.dict_fxn_t_bar_min_rpm.update(self.dict_fxn_t_bar_min_rpm_local)
        self.dict_fxn_t_p_min_rpm.update(self.dict_fxn_t_p_min_rpm_local)
        self.dict_fxn_c.update(self.dict_fxn_c_local)
        self.dict_fxn_s_ib_single_j_iterating.update(self.dict_fxn_s_ib_single_j_iterating_local)

        #Pull
        self.dict_fxn_s_ib_single_i_local.update(self.dict_fxn_s_ib_single_i)
        self.dict_fxn_s_ib_single_i_apx_local.update(self.dict_fxn_s_ib_single_i_apx)
        self.dict_fxn_demand_irf_local.update(self.dict_fxn_demand_irf)
        self.dict_fxn_t_bar_min_irf_local.update(self.dict_fxn_t_bar_min_irf)
        self.dict_fxn_demand_if_local.update(self.dict_fxn_demand_if)
        self.dict_fxn_t_bar_ma_local.update(self.dict_fxn_t_bar_ma)
        self.dict_fxn_r_ij_local.update(self.dict_fxn_r_ij)
        self.dict_fxn_t_bar_min_index_link_local.update(self.dict_fxn_t_bar_min_index_link)
        self.dict_fxn_t_bar_min_index_local.update(self.dict_fxn_t_bar_min_index)
        self.dict_fxn_miat_t_i_b_single_local.update(self.dict_fxn_miat_t_i_b_single)
        self.dict_fxn_peak_speed_rpm_rpm_local.update(self.dict_fxn_peak_speed_rpm_rpm)
        self.dict_fxn_t_bar_min_rpm_local.update(self.dict_fxn_t_bar_min_rpm)
        self.dict_fxn_t_p_min_rpm_local.update(self.dict_fxn_t_p_min_rpm)
        self.dict_fxn_c_local.update(self.dict_fxn_c)
        self.dict_fxn_s_ib_single_j_iterating_local.update(self.dict_fxn_s_ib_single_j_iterating)


    def print_output_signature(self,use_irf_analytic_miat,elimination,print_progress,eff,apx):

        """Print message about APX_EXACT_24 config to terminal"""

        output_sig = ""

        if use_irf_analytic_miat:
            output_sig += "IRF-"

        if elimination:
            output_sig += "elim-"

        if print_progress:
            output_sig += "print-"

        if eff:
            output_sig +="eff-"

        if apx:
            output_sig += "approx-"

        if output_sig != "":
            print(output_sig)

if __name__ == '__main__':

    #Unit Tests
    UT_OMEGA = [0,1,2,3,4,5]
    UT_WCET = [0,50,40,30,20,10]
    UT_ALPHA = 10
    UT_M = len(UT_OMEGA)-1
    UT_AVR_TSK = AVR_TASK.AvrTask(UT_M,UT_OMEGA,UT_WCET,UT_ALPHA,"unit_test")
    UT_APX_EXT = ApxExact24(UT_AVR_TSK,None,1,0)

    # def fxn_assert_omega_indices(self,i,j):
    UT_APX_EXT.fxn_assert_omega_indices(1,2)

    # def fxn_assert_omega_rpms(self,omega_i,omega_j):
    UT_APX_EXT.fxn_assert_omega_indices(4,5)

    # def fxn_c(self,s):
    retval = UT_APX_EXT.fxn_c(2.5)
    assert retval == 30

    # def fxn_c_binary(self,s):
    retval = UT_APX_EXT.fxn_c_binary(2.5)
    assert retval == 30

    # def fxn_c_linear(self,s):
    retval = UT_APX_EXT.fxn_c_binary(2.5)
    assert retval == 30

    # def fxn_theta(self,i,j):
    retval = UT_APX_EXT.fxn_theta(1,2)
    assert retval == (UT_OMEGA[2]**2 - UT_OMEGA[1]**2)/(2*UT_ALPHA)

    # def fxn_t_min_rpm(self,omega_i,omega_j):
    retval = UT_AVR_TSK.fxn_t_min_rpm(1,2)
    assert retval == (math.sqrt(2*2**2 + 4*UT_ALPHA + 2*1**2) - 2 - 1)/UT_ALPHA

    # def fxn_omega_rb(self,i,r):
    retval = UT_APX_EXT.fxn_omega_rb(2,12)
    assert retval == [UT_OMEGA[2]]*12

    # def fxn_omega_ma(self,i,f):
    retval = UT_APX_EXT.fxn_omega_ma(2,2)
    assert retval == [UT_OMEGA[2],
                        math.sqrt(UT_OMEGA[2]**2+2*UT_ALPHA*1)]

    # def fxn_r(self,i,j):
    retval = UT_APX_EXT.fxn_r(2,UT_AVR_TSK.m)
    assert retval == math.ceil(UT_APX_EXT.fxn_theta(2,UT_AVR_TSK.m))

    # def fxn_omega_irf(self,i,r,f):
    retval = UT_APX_EXT.fxn_omega_irf(2,12,2)
    rb = [UT_OMEGA[2]]*12
    ma = [UT_OMEGA[2],
            math.sqrt(UT_OMEGA[2]**2+2*UT_ALPHA*1)]
    assert retval == (rb + ma)

    #MIAT methods comparison
    miat_seq_irf_elim = UT_APX_EXT.fxn_t_ib(UT_AVR_TSK.m,200,True,True)
    UT_APX_EXT.fxn_reset_all_tables()
    miat_seq_elim = UT_APX_EXT.fxn_t_ib(UT_AVR_TSK.m,200,False,True)
    UT_APX_EXT.fxn_reset_all_tables()
    miat_seq_none = UT_APX_EXT.fxn_t_ib(UT_AVR_TSK.m,200,False,False)
    UT_APX_EXT.fxn_reset_all_tables()
    assert miat_seq_irf_elim[0] == miat_seq_elim[0]
    assert miat_seq_elim[0] == miat_seq_none[0]

    # def fxn_reset_k_and_k_based_tables(self):
    UT_AVR_TSK.k = 500
    UT_APX_EXT.fxn_reset_k_and_k_based_tables()
    assert UT_AVR_TSK.k == -1
