"""Create slurm script for executing python experiments"""

import sys


# python3 slurm_script_writer.py var_prec-row17_12_0_0.sh var_prec-row17_12_0_0 200 var_prec row17 5 1 0 0 0 0
slurm_ram_gb = int(sys.argv[1])
experiment = sys.argv[2]
algorithm =  sys.argv[3]
task_set = int(sys.argv[4])
precision =  int(sys.argv[5])
memoize =  int(sys.argv[6])
give_sln_seq =  int(sys.argv[7])
trace_memory =  int(sys.argv[8])
cores =  int(sys.argv[9])
parallel_type = int(sys.argv[10])

precision_str = str(precision)
if precision <= 9:
    precision_str = "0"+str(precision)

cores_str = str(cores)
if cores <= 9:
    cores_str = "0"+str(cores)

slurm_script_filename_base_vals = [experiment,algorithm]
slurm_script_filename_para_vals = ["k"+str(task_set),
                                   "d"+precision_str,
                                   "m"+str(memoize),
                                   "s"+str(give_sln_seq),
                                   "t"+str(trace_memory),
                                   "c"+cores_str,
                                   "p"+str(parallel_type)]

slurm_script_filename = ""
for string in slurm_script_filename_base_vals:
    slurm_script_filename += string + "-"

for string in slurm_script_filename_para_vals:
    slurm_script_filename += string

slurm_script_filename_sh = slurm_script_filename+".sh"

sl_scr_fh = open(slurm_script_filename_sh,'w',encoding="utf8")

output = "#!/bin/bash" + "\n"
output += "# Job name" + "\n"
output += "#SBATCH --job-name " + slurm_script_filename + "\n"
output += "# Submit to the primary QoS" + "\n"
output += "#SBATCH -q primary" + "\n"
output += "# Request one node" + "\n"
output += "#SBATCH -N 1" + "\n"
output += "# Total number of cores, in this example it will 1 node with 1 core each. " + "\n"
output += "#SBATCH -n " + str(cores) + "\n"
output += "# Request memory" + "\n"
output += "#SBATCH --mem=" + str(slurm_ram_gb) + "GB" + "\n"
output += "# Mail when the job begins, ends, fails, requeues " + "\n"
output += "#SBATCH --mail-type=FAIL" + "\n"
output += "# Where to send email alerts" + "\n"
output += "#SBATCH --mail-user=ANON@ANON.EDU" + "\n"
output += "# Create an output file that will be output_<jobid>.out " + "\n"
output += "#SBATCH -o output_%j.out" + "\n"
output += "# Create an error file that will be error_<jobid>.out" + "\n"
output += "#SBATCH -e errors_%j.err" + "\n"
output += "# Set maximum time limit " + "\n"
if experiment == "v_m":
    output += "#SBATCH -t 0-15:00:00" + "\n"
else:
    output += "#SBATCH -t 0-2:00:00" + "\n"
if trace_memory:
    output += "# Set pref to MEM cluster" + "\n"
    output += "#SBATCH -w mem[1-9]" + "\n"
else:
    output += "# Set pref to MDT cluster" + "\n"
    output += "#SBATCH -w mdt[1-83]" + "\n"
output += "\n"
output += "python3 " + experiment + "-flex-parser.py "
output += algorithm + " "
if experiment == "v_pre" or experiment == "v_acc" or experiment == "v_dur" or experiment == "v_dur_para":
    output += str(task_set) + " "
output += str(precision) + " "
output += str(memoize) + " "
output += str(give_sln_seq) + " "
output += str(trace_memory) + " "
output += str(cores) + " "
output += str(parallel_type)
output += "\n"

sl_scr_fh.write(output)
