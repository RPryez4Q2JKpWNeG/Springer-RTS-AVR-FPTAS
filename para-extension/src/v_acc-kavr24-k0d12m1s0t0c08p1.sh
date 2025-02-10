#!/bin/bash
# Job name
#SBATCH --job-name v_acc-kavr24-k0d12m1s0t0c08p1
# Submit to the primary QoS
#SBATCH -q primary
# Request one node
#SBATCH -N 1
# Total number of cores, in this example it will 1 node with 1 core each. 
#SBATCH -n 8
# Request memory
#SBATCH --mem=32GB
# Mail when the job begins, ends, fails, requeues 
#SBATCH --mail-type=FAIL
# Where to send email alerts
#SBATCH --mail-user=ANON@ANON.EDU
# Create an output file that will be output_<jobid>.out 
#SBATCH -o output_%j.out
# Create an error file that will be error_<jobid>.out
#SBATCH -e errors_%j.err
# Set maximum time limit 
#SBATCH -t 0-2:00:00
# Set pref to MDT cluster
#SBATCH -w mdt[1-83]

python3 v_acc-flex-parser.py kavr24 0 12 1 0 0 8 1
