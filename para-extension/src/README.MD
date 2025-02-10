# PDS BPCKP Experiment Run Instructions

## On a standalone device (e.g., your laptop)

1. Execute python3 v_XXX-flex-parser.py ALG TASKSET PRECISION MEMOIZATION SLN_SEQ_PROD MEM_TRACE NCORES PARA_TYPE
where:
- ALG = apx, kavr24, exact, OR row17
- TASKSET = 0 (Canonical, CAN) OR 1 (Generalized, GEN)
- PRECISION = 1-12
- MEMOIZATION = 0 (Do not use memoization) OR 1 (Use memoization)
- SLN_SEQ_PROD = 0 (Do not produce the sequence generating maximum demand) OR 1 (Produce the sequence generating maximum demand)
- MEM_TRACE = 1
- NCORES = # (The number of cores you wish to allow the algorithm to use)
- PARA_TYPE = 0 (Parallelization by Demand Interval - PBI) OR 1 (Parallelization by Mode - PBM)

Example 1:

The command
```
python3 v_acc-flex-parser.py apx 0 12 1 0 0 1 0
```
will run the variable acceleration experiment with:
- Algorithm: apx (APX)
- Task: 0 (Canonical - CAN)
- Precision: 12 (12 positions after the decimal)
- Memoization: 1 (Yes, use memoization)
- Solution Sequence Production: 0 (No, do not produce the solution sequence, only the demand value)
- Memory Tracing: 0 (No, do not trace memory for determing memory usage)
- Number of Cores: 1 (Use only 1 processor core)
- Parallelization Type: 0 (Use Parallelization by Demand Interval - PBI) *Note, this is ignored when a single core is used*

Example 2:

The command
```
python3 v_dur-flex-parser.py kavr24 1 5 1 0 0 4 1
```
will run the variable duration experiment with:
- Algorithm: kavr24 (KAVR)
- Task: 1 (Generalized - GEN)
- Precision: 5 (5 positions after the decimal)
- Memoization: 1 (Yes, use memoization)
- Solution Sequence Production: 0 (No, do not produce the solution sequence, only the demand value)
- Memory Tracing: 0 (No, do not trace memory for determing memory usage)
- Number of Cores: 4 (Use 4 processor cores)
- Parallelization Type: 1 (Use Parallelization by Demand Mode - PBM) *Note, this is ignored when a single core is used*

2. Review results in the exp_data/ folder

## On a SLURM Workload Manager-equipped HPC Grid (e.g., your organizations HPC)

***Warning: Remember to edit the shell scripts within this project respect your HPC grid's memory limits, node names, submission policies, etc.***

1. Copy this entire directory to your HPC grid's starter/launcher/primary node
2. Execute HPC-BASH-create-all.sh to generate all experiment SLURM scripts
3. Execute HPC-BASH-sbatch-all.sh to SBATCH submit all jobs to your SLURM workload manager
4. Review results in the exp_data/ folder
*Note, you may customize the auto-generated scripts by editing any *.sh file using the descriptions in the "On a standalone device" section above*

# To explore source code

1. Literature implementations can be found in bpckp_fxns/*
   1. KAVR = kavr_24.py
   2. EXACT = bpckp_fptas.py:calculate_demand_seq() with apx = 0
   2. APX = bpckp_fptas.py:calculate_demand_seq() with apx = 1
   3. ROW = row_17.py - Implementation of Mohaqeqi et al. "Refinement of Workload..." from ECRTS'17

# Brief Summary
1.  apx_fxns/ - Contains classes, functions required for APX execution
2.  avr_fxns/ - Defines AVR tasks and tools to generate AVR tasks
3.  bpckp_fxns/ - Defines demand calculation algorithms
4.  csv_fxns/ - Tools for exporting to CSV
5.  exp_data/ - Location for experimental data to be placed, source of GNUPLOT data for creating figures
    1.  exp_data/pub_data/ - Raw data used to create aggregate data files with timestamps
6.  outpit_file_name_gen/ - Tool for create filenames based on experiment
7.  sxs_fxns/ - Functions for running experiments with different demand calculation algorithms
8.  task_sets/ - Classes of task sets from literature, from random generations, and for validation testing
9.  HPC-BASH-* - Scripts to generate (HPC-BASH-create-*), batch submit (HPC-BASH-sbatch-all.sh), and delete (HPC-BASH-delete-all.sh) SLURM run scripts for HPC grid (requires modification for node names)
10. v_XXX-* - An experiment for testing variable XXX versus runtime where XXX:
    1.  pre = precision
    2.  dur = duration
    3.  acc = acceleration
    4.  m = mode quantity
11. var_ar-sln-qual.py - An experiment for testing variable approximation ratios affect on solution quality.
11. var_ar-runtime.py - An experiment for testing variable approximation ratios affect on runtime.