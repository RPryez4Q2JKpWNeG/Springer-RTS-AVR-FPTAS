"""
PDS BPCKP Experiment
"""

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
    PRECISION = 12
    MEMOIZE = 1
    TRACE_MEMORY = 0
    GIVE_SLN_SEQ = 0
    N_CORES = 0
    PARA_TYPE = 1

#pylint: disable=C0200,C0301

EXPERIMENT_NAME = "var_accel"

#Create algorithm parameters
APX_PARAMS = apx_obj.ApxObj(0.025,0.025,0.025)

#Create can task sets
lit_task_set = lit_avr_task_sets.LitAvrTaskSets()

if TASK_SET == 0:
    task_set = lit_task_set.avr_task_instance_2018_existing
else:
    task_set = lit_task_set.avr_task_instance_2018_general

#Create accel set
BASE_ACCELERATION = 10000
ACCEL_SET = []
for i in range(100):
    ACCEL_SET += [BASE_ACCELERATION*(i+1)]

delta_times_us = [1000000]
alg_delta_set = delta_set.DeltaSet(delta_times_us,"1s")

#Set verbosity
VERBOSE = 0

alg_params = avr_alg_params.AvrAlgParams(PRECISION,MEMOIZE,GIVE_SLN_SEQ,TRACE_MEMORY,APX_PARAMS,N_CORES,PARA_TYPE)

#Task Set alterations
var_precision_alg_exp_tsk_set = [-1]*len(ACCEL_SET)

for i in range(len(ACCEL_SET)):
    var_precision_alg_exp_tsk_set[i] = exp_task.ExperimentTask(ALGORITHM,alg_params,task_set,alg_delta_set,VERBOSE)
    var_precision_alg_exp_tsk_set[i].avr_task_instance.alpha = ACCEL_SET[i]

exp_runner_instance = exp_runner.ExperimentRunner()

MAKE_DBF_LOG_FILE = False
MAKE_EXP_LOG_FILE = True
MAKE_AGG_LOG_FILE = True

#Run experiment
exp_runner_instance.run_experiments(var_precision_alg_exp_tsk_set,MAKE_DBF_LOG_FILE,MAKE_EXP_LOG_FILE,MAKE_AGG_LOG_FILE,EXPERIMENT_NAME,VERBOSE)
