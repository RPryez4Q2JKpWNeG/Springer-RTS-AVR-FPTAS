"""Combine last lines of same experiment-algorithm data files"""

import subprocess

DEBUG = 0

# pylint: disable=C0200

experiment_names = ["precision"]
algorithms = ["row17","kavr24","exact","apx"]
precisions = [5,6,7,8,9,10,11,12]
task_sets = ["can","gen"]
param_short_names = ["rtss18"]
n_cores_arr = [1,2,4,8,16]
para_types = [0,1]

#Desired outcome?
## Group the total runtime (i.e., last row) of all precisions into one file
## The last rows should share the same task set, core count, and para type

for exp in experiment_names:
    for param_short_name in param_short_names:
        for alg in algorithms:
            for task_set in task_sets:
                for para_type in para_types:

                    # if alg == "apx" and para_type == 1:
                    #     continue

                    for cores in n_cores_arr:

                        cores_str = str(cores)
                        if int(cores) <= 9:
                            cores_str = "0"+str(cores)

                        #Create output file
                        OUTPUT_FILE_NAME = "v_"+str(exp)+"-"+str(alg)+"-p05-p12-"+str(task_set)+"-"+str(param_short_name)+"-m1-s0-t0-c"+cores_str+"-p"+str(para_type)+".csv"
                        output_csv_hdl = open(str(OUTPUT_FILE_NAME),"w",10, encoding="utf-8")

                        lines_written = 0
                        header_written = 0

                        for precision in precisions:

                            if (alg == "apx" or alg == "exact") and precision != 12:
                                continue

                            precision_str = str(precision)
                            if precision <= 9:
                                precision_str = "0"+str(precision)

                            cores_str = str(cores)
                            if int(cores) <= 9:
                                cores_str = "0"+str(cores)

                            if cores == 1:
                                INPUT_FILE_NAME = "var_"+str(exp)+"-"+str(alg)+"-p"+precision_str+"-"+str(task_set)+"-"+str(param_short_name)+"-m1-s0-t0-c"+cores_str+"-p0-ES.csv"
                            else:
                                INPUT_FILE_NAME = "var_"+str(exp)+"-"+str(alg)+"-p"+precision_str+"-"+str(task_set)+"-"+str(param_short_name)+"-m1-s0-t0-c"+cores_str+"-p"+str(para_type)+"-ES.csv"

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

