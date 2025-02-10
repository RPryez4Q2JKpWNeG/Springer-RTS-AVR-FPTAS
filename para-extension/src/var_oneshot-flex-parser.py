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
    PRECISION = int(sys.argv[2])
    MEMOIZE = int(sys.argv[3])
    GIVE_SLN_SEQ = int(sys.argv[4])
    TRACE_MEMORY = int(sys.argv[5])
    N_CORES = int(sys.argv[6])
    PARA_TYPE = int(sys.argv[7])
else:
    ALGORITHM = "row17"
    PRECISION = 5
    MEMOIZE = 1
    GIVE_SLN_SEQ = 0
    TRACE_MEMORY = 0
    N_CORES = 1

#Create algorithm parameters
APX_PARAMS = apx_obj.ApxObj(0.025,0.025,0.025)

#Create task set
lit_task_set = lit_avr_task_sets.LitAvrTaskSets()
task_set_can = lit_task_set.avr_task_instance_2018_existing
task_set_gen = lit_task_set.avr_task_instance_2018_general

#Create delta set
START_DELTA_US = 10000
INCREMENT_DELTA_US = 10000
END_DELTA_US = 10000
alg_delta_set = delta_set.DeltaSet([0],"rtss18")
alg_delta_set.update_delta_set_with_range(START_DELTA_US,INCREMENT_DELTA_US,END_DELTA_US)

#Set verbosity
VERBOSE = 0

alg_params = avr_alg_params.AvrAlgParams(PRECISION,MEMOIZE,GIVE_SLN_SEQ,TRACE_MEMORY,APX_PARAMS,N_CORES,PARA_TYPE)

var_oneshot_can = exp_task.ExperimentTask(ALGORITHM,alg_params,task_set_can,alg_delta_set,VERBOSE)
# var_oneshot_gen = exp_task.ExperimentTask(ALGORITHM,alg_params,task_set_gen,alg_delta_set,VERBOSE)

exp_runner_instance = exp_runner.ExperimentRunner()

MAKE_DBF_LOG_FILE = False
MAKE_EXP_LOG_FILE = False
MAKE_AGG_LOG_FILE = True

exp_runner_instance.run_experiments([var_oneshot_can],MAKE_DBF_LOG_FILE,MAKE_EXP_LOG_FILE,MAKE_AGG_LOG_FILE,"var_precision",VERBOSE)
# exp_runner_instance.run_experiments([var_oneshot_gen],MAKE_DBF_LOG_FILE,MAKE_EXP_LOG_FILE,MAKE_AGG_LOG_FILE,"var_precision",VERBOSE)
