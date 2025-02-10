# README
This repo contains anonymized source code for the RTNS'24 paper:
"A Fully Polynomial Time Approximation Scheme for Adaptive Variable Rate Task Demand"

## PDS BPCKP Experiment Run Instructions

1. Identify an experiment from the src/* folder level (e.g., var_prec-kavr_24-p05.py) you wish to run
2. Execute python3 var_prec-kavr_24-p05.py
3. Allow simulation to finish
4. Review results in exp_data folder

## To explore source code

1. Literature implementations can be found in bpckp_fxns/*
   1. KAVR = KAVR_24.py
   2. EXACT = bpckp_fptas.py:calculate_demand_seq() with apx = 0
   2. APX = bpckp_fptas.py:calculate_demand_seq() with apx = 1
2. Mohaqeqi et al. "Refinement of Workload..." from ECRTS'17 is also implemented as ROW_17.py

## Brief Summary
1.  apx_fxns/ - Contains classes, functions required for APX execution
2.  avr_fxns/ - Defines AVR tasks and tools to generate AVR tasks
3.  bpckp_fxns/ - Defines demand calculation algorithms
4.  csv_fxns/ - Tools for exporting to CSV
5.  exp_data/ - Location for experimental data to be placed, source of GNUPLOT data for creating figures
    1.  exp_data/pub_data/ - Raw data used to create aggregate data files with timestamps
6.  outpit_file_name_gen/ - Tool for create filenames based on experiment
7.  sxs_fxns/ - Functions for running experiments with different demand calculation algorithms
8.  task_sets/ - Classes of task sets from literature, from random generations, and for validation testing
9.  HPC-BASH-* - Scripts to run on a SLURM-capable HPC grid (requires modification for node names)
10. HPC-SBATCH-* - Scripts to call with SBATCH on a SLURM-capable HPC grid (requires modification for node names)
11. var_XXX-* - An experiment for testing variable XXX versus runtime where XXX:
    1.  prec = precision
    2.  dur = duration
    3.  accel = acceleration
    4.  m = mode quantity
12. var_XXX-*-mem - An experiment for testing variable XXX for peak memory usage
13. var_XXX-kavr_24-pYY-* - An experiment for testing variable XXX using KAVR'24 with precision YY