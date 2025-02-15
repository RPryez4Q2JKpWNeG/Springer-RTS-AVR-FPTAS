"""
PDS BPCKP Experiment
"""

import copy

from sxs_fxns import exp_runner
from sxs_fxns import exp_task
from sxs_fxns import avr_alg_params
from sxs_fxns import delta_set
from apx_fxns import apx_obj
from task_sets import mode_16_model as MODE16_EXP

import sys  #Read commands

#pylint: disable=C0200,C0301

#Create experiment params
EXPERIMENT_NAME = "var_mode_16"
VERBOSE = 0

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
    ALGORITHM = "kavr24"
    PRECISION = 12
    MEMOIZE = 1
    GIVE_SLN_SEQ = 0
    TRACE_MEMORY = 0
    N_CORES = 1
    PARA_TYPE = 0

#Create algorithm parameters
APX_PARAMS = apx_obj.ApxObj(0.025,0.025,0.025)

alg_params = avr_alg_params.AvrAlgParams(PRECISION,MEMOIZE,GIVE_SLN_SEQ,TRACE_MEMORY,APX_PARAMS,N_CORES,PARA_TYPE)

#Create tasks
mode16_exp_instance = MODE16_EXP.UserTaskSet()
task_set = mode16_exp_instance.avr_task_instance_user_task_set

var_m_task_sets = [-1]*(16-1)
var_m_task_sets[0] = copy.deepcopy(task_set)

for i in range(1,len(var_m_task_sets)):
    var_m_task_sets[i] = copy.deepcopy(var_m_task_sets[i-1])

    #delete middle WCET
    var_m_task_sets[i].wcet = copy.deepcopy(var_m_task_sets[i].wcet)
    length = len(var_m_task_sets[i].wcet)
    middle_index = length//2
    var_m_task_sets[i].wcet.remove(var_m_task_sets[i].wcet[middle_index])

    #delete middle omega
    var_m_task_sets[i].omega = copy.deepcopy(var_m_task_sets[i].omega)
    var_m_task_sets[i].omega.remove(var_m_task_sets[i].omega[middle_index])

    #reduce m by one
    var_m_task_sets[i].m = copy.deepcopy(var_m_task_sets[i].m-1)


#Create delta set
delta_set_us = [750000] #0.75s
alg_delta_set = delta_set.DeltaSet(delta_set_us,"750ms")

#Variable
VAR_M_SETS = var_m_task_sets
var_m_alg_exp_set = [-1]*len(VAR_M_SETS)


for i in range(len(VAR_M_SETS)):

    var_m_alg_exp_set[i] = exp_task.ExperimentTask(ALGORITHM,alg_params,var_m_task_sets[i],alg_delta_set,VERBOSE)

exp_runner_instance = exp_runner.ExperimentRunner()

MAKE_DBF_LOG_FILE = False
MAKE_EXP_LOG_FILE = True
MAKE_AGG_LOG_FILE = True

exp_runner_instance.run_experiments(var_m_alg_exp_set,MAKE_DBF_LOG_FILE,MAKE_EXP_LOG_FILE,MAKE_AGG_LOG_FILE,EXPERIMENT_NAME,VERBOSE)
