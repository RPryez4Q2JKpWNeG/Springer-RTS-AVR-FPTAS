"""
PDS BPCKP Experiment
"""

import math

from sxs_fxns import exp_runner
from sxs_fxns import exp_task
from sxs_fxns import avr_alg_params
from sxs_fxns import delta_set
from task_sets import lit_avr_task_sets
from apx_fxns import apx_obj

import sys  #Read commands

#Command template
if len(sys.argv) >= 6:
    ALGORITHM = sys.argv[1]
    TASK_SET = int(sys.argv[2])
    PRECISION = int(sys.argv[3])
    MEMOIZE = int(sys.argv[4])
    GIVE_SLN_SEQ = int(sys.argv[5])
    TRACE_MEMORY = int(sys.argv[6])
    N_CORES = int(sys.argv[7])
    PARA_TYPE = int(sys.argv[8])
else:
    ALGORITHM = "apx"
    TASK_SET = 0
    PRECISION = 5
    MEMOIZE = True
    GIVE_SLN_SEQ = False
    TRACE_MEMORY = False
    N_CORES = 2
    PARA_TYPE = 1

EXPERIMENT_NAME = "var_duration"

#Create algorithm parameters
APX_PARAMS = apx_obj.ApxObj(0.025,0.025,0.025)

#Create can task sets
lit_task_set = lit_avr_task_sets.LitAvrTaskSets()

if TASK_SET == 0:
    task_set = lit_task_set.avr_task_instance_2018_existing
else:
    task_set = lit_task_set.avr_task_instance_2018_general

#Create delta set
START_DELTA_US = 10000
POWERS = 4
INDICES = 5

delta_times_us = []

for i in range(POWERS):
    for j in range(INDICES):
        delta_times_us += [START_DELTA_US*int(math.pow(10,i))*(j+1)]

CUTOFF = 11
delta_times_us = delta_times_us[:CUTOFF]

#Set verbosity
VERBOSE = 0

alg_params = avr_alg_params.AvrAlgParams(PRECISION,MEMOIZE,GIVE_SLN_SEQ,TRACE_MEMORY,APX_PARAMS,N_CORES,PARA_TYPE)

var_duration_alg_exp_tsk_arr = [-1]*len(delta_times_us)

for i in range(len(delta_times_us)):
    alg_delta_set = delta_set.DeltaSet([delta_times_us[i]],"1.0e6-set")
    var_duration_alg_exp_tsk_arr[i] = exp_task.ExperimentTask(ALGORITHM,alg_params,task_set,alg_delta_set,VERBOSE)

exp_runner_instance = exp_runner.ExperimentRunner()

make_dbf_log_file = False
make_exp_log_file = True
make_agg_log_file = True

exp_runner_instance.run_experiments(var_duration_alg_exp_tsk_arr,make_dbf_log_file,make_exp_log_file,make_agg_log_file,EXPERIMENT_NAME,VERBOSE)
