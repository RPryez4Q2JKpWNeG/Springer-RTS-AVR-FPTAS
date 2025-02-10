"""Combine last lines of same experiment-algorithm data files"""

import subprocess

DEBUG = 0

# pylint: disable=C0200

exp = "duration"
algorithms = ["exact","apx"]
precision = 12
task_sets = ["can","gen"]
param_short_name = "1.0e6-set"
cores = [1,2,4,8,16]
para_type = 1

#Desired outcome?
## Group the total runtime (i.e., last row) of all precisions into one file
## The last rows should share the same task set, core count, and para type

for alg in algorithms:
    for task_set in task_sets:
        #Create output file
        OUTPUT_FILE_NAME = "v_"+str(exp)+"-"+str(alg)+"-p12-"+str(task_set)+"-"+str(param_short_name)+"-m1-s0-t0-c01-16-p"+str(para_type)+".csv"
        output_csv_hdl = open(str(OUTPUT_FILE_NAME),"w",10, encoding="utf-8")

        lines_written = 0
        header_written = 0

        for core in cores:

            if core == 1:
                INPUT_FILE_NAME = "var_"+str(exp)+"-"+str(alg)+"-p"+str(precision)+"-"+str(task_set)+"-"+str(param_short_name)+"-m1-s0-t0-c"+str(core)+"-p0-ES.csv"
            else:
                INPUT_FILE_NAME = "var_"+str(exp)+"-"+str(alg)+"-p"+str(precision)+"-"+str(task_set)+"-"+str(param_short_name)+"-m1-s0-t0-c"+str(core)+"-p"+str(para_type)+"-ES.csv"

            if DEBUG:
                INPUT_FILE_NAME = "src/exp_data/" + INPUT_FILE_NAME
                print(INPUT_FILE_NAME)

            if not header_written:

                try:
                    head_line = subprocess.check_output(['head','-n','1',INPUT_FILE_NAME])
                
                    head_line = str(head_line)
                    head_line = head_line[2:]
                    head_line = head_line[:-3]

                    output_csv_hdl.write(head_line)
                    output_csv_hdl.write('\n')

                    header_written = 1

                except subprocess.CalledProcessError as e:
                    pass

            try:
                tail_line = subprocess.check_output(['tail', '-n', '1', INPUT_FILE_NAME])

                tail_line = str(tail_line)
                tail_line = tail_line[2:]
                tail_line = tail_line[:-3]

                output_csv_hdl.write(tail_line)
                output_csv_hdl.write('\n')

                lines_written += 1

            except subprocess.CalledProcessError as e:
                pass
                # print("No file: ",source_data_file_name)

        output_csv_hdl.close()

        if lines_written == 0:
            subprocess.check_output(['rm',OUTPUT_FILE_NAME])

