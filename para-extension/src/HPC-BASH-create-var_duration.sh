#! /bin/bash

#RAM - ALG - EXPERIMENT - TSK - M/S/T/Core/Para Type
#KAVR
python3 slurm_script_writer.py 32 v_dur_para kavr24 0 05 1 0 0 01 0
python3 slurm_script_writer.py 32 v_dur_para kavr24 0 05 1 0 0 02 1
python3 slurm_script_writer.py 32 v_dur_para kavr24 0 05 1 0 0 04 1
python3 slurm_script_writer.py 32 v_dur_para kavr24 0 05 1 0 0 08 1

python3 slurm_script_writer.py 32 v_dur_para kavr24 0 12 1 0 0 01 0
python3 slurm_script_writer.py 32 v_dur_para kavr24 0 12 1 0 0 02 1
python3 slurm_script_writer.py 32 v_dur_para kavr24 0 12 1 0 0 04 1
python3 slurm_script_writer.py 32 v_dur_para kavr24 0 12 1 0 0 08 1

python3 slurm_script_writer.py 32 v_dur_para kavr24 1 05 1 0 0 01 0
python3 slurm_script_writer.py 32 v_dur_para kavr24 1 05 1 0 0 02 1
python3 slurm_script_writer.py 32 v_dur_para kavr24 1 05 1 0 0 04 1
python3 slurm_script_writer.py 32 v_dur_para kavr24 1 05 1 0 0 08 1

python3 slurm_script_writer.py 32 v_dur_para kavr24 1 12 1 0 0 01 0
python3 slurm_script_writer.py 32 v_dur_para kavr24 1 12 1 0 0 02 1
python3 slurm_script_writer.py 32 v_dur_para kavr24 1 12 1 0 0 04 1
python3 slurm_script_writer.py 32 v_dur_para kavr24 1 12 1 0 0 08 1

#EXACT
python3 slurm_script_writer.py 32 v_dur_para exact 0 12 1 0 0 01 0
python3 slurm_script_writer.py 32 v_dur_para exact 0 12 1 0 0 02 1
python3 slurm_script_writer.py 32 v_dur_para exact 0 12 1 0 0 04 1
python3 slurm_script_writer.py 32 v_dur_para exact 0 12 1 0 0 08 1

python3 slurm_script_writer.py 32 v_dur_para exact 1 12 1 0 0 01 0
python3 slurm_script_writer.py 32 v_dur_para exact 1 12 1 0 0 02 1
python3 slurm_script_writer.py 32 v_dur_para exact 1 12 1 0 0 04 1
python3 slurm_script_writer.py 32 v_dur_para exact 1 12 1 0 0 08 1

#APX
python3 slurm_script_writer.py 32 v_dur_para apx 0 12 1 0 0 01 0
python3 slurm_script_writer.py 32 v_dur_para apx 0 12 1 0 0 02 1
python3 slurm_script_writer.py 32 v_dur_para apx 0 12 1 0 0 04 1
python3 slurm_script_writer.py 32 v_dur_para apx 0 12 1 0 0 08 1

python3 slurm_script_writer.py 32 v_dur_para apx 1 12 1 0 0 01 0
python3 slurm_script_writer.py 32 v_dur_para apx 1 12 1 0 0 02 1
python3 slurm_script_writer.py 32 v_dur_para apx 1 12 1 0 0 04 1
python3 slurm_script_writer.py 32 v_dur_para apx 1 12 1 0 0 08 1