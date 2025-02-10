"""Combine last lines of same experiment-algorithm data files"""

import subprocess
import os

DEBUG = 0

# pylint: disable=C0200

experiment_names = ["precision"]
task_sets = [["can","gen"]]
param_short_names = ["rtss18"]
algorithms = ["kavr24"]
cores = [1,2,4,8]
para_types = [0,1]
precisions = [5,6,7,8,9,10,11,12]

for i in range(len(experiment_names)):
    exp = experiment_names[i]
    param_short_name = param_short_names[i]
    print(str(exp)+"-"+str(param_short_name))
    for alg in algorithms:
        for task_set in task_sets[i]:
            for para_type in para_types:
                for core in cores:

                    #Create output file
                    output_file_name = "v_"+str(exp)+"-"+str(alg)+"-p05-p12-"+str(task_set)+"-"+str(param_short_name)+"-m1-s0-t0-c"+str(core)+"-p"+str(para_type)+".csv"
                    output_csv_hdl = open(str(output_file_name),"w",10, encoding="utf-8")

                    for precision in precisions:

                        if core == 1:
                            source_data_file_name = "var_"+str(exp)+"-"+str(alg)+"-p"+str(precision)+"-"+str(task_set)+"-"+str(param_short_name)+"-m1-s0-t0-c"+str(core)+"-p0-AG.csv"
                        else:
                            source_data_file_name = "var_"+str(exp)+"-"+str(alg)+"-p"+str(precision)+"-"+str(task_set)+"-"+str(param_short_name)+"-m1-s0-t0-c"+str(core)+"-p"+str(para_type)+"-AG.csv"

                        if DEBUG:
                            source_data_file_name = "src/exp_data/" + source_data_file_name
                            print(source_data_file_name)

                        lines_written = 0

                        try:
                            line = subprocess.check_output(['tail', '-n', '1', source_data_file_name])

                            line_str = str(line)

                            line_str = line_str[2:]
                            line_str = line_str[:-3]

                            output_csv_hdl.write(line_str)
                            output_csv_hdl.write('\n')

                            lines_written += 1

                        except subprocess.CalledProcessError as e:
                            pass
                            # print("No file: ",source_data_file_name)

                output_csv_hdl.close()

            if lines_written == 0:

                subprocess.check_output(['rm',output_file_name])

