#! /bin/bash

#RAM - ALG - EXPERIMENT - TSK - M/S/T/Core/Para Type
#KAVR
python3 slurm_script_writer.py 32 v_m kavr24 0 05 1 0 0 01 0
python3 slurm_script_writer.py 32 v_m kavr24 0 05 1 0 0 02 1
python3 slurm_script_writer.py 32 v_m kavr24 0 05 1 0 0 04 1
python3 slurm_script_writer.py 32 v_m kavr24 0 05 1 0 0 08 1
python3 slurm_script_writer.py 32 v_m kavr24 0 05 1 0 0 16 1

python3 slurm_script_writer.py 32 v_m kavr24 0 12 1 0 0 01 0
python3 slurm_script_writer.py 32 v_m kavr24 0 12 1 0 0 02 1
python3 slurm_script_writer.py 32 v_m kavr24 0 12 1 0 0 04 1
python3 slurm_script_writer.py 32 v_m kavr24 0 12 1 0 0 08 1
python3 slurm_script_writer.py 32 v_m kavr24 0 12 1 0 0 16 1

#EXACT
python3 slurm_script_writer.py 32 v_m exact 0 12 1 0 0 01 0
python3 slurm_script_writer.py 32 v_m exact 0 12 1 0 0 02 1
python3 slurm_script_writer.py 32 v_m exact 0 12 1 0 0 04 1
python3 slurm_script_writer.py 32 v_m exact 0 12 1 0 0 08 1
python3 slurm_script_writer.py 32 v_m exact 0 12 1 0 0 16 1

#APX
python3 slurm_script_writer.py 32 v_m apx 0 12 1 0 0 01 0
python3 slurm_script_writer.py 32 v_m apx 0 12 1 0 0 02 1
python3 slurm_script_writer.py 32 v_m apx 0 12 1 0 0 04 1
python3 slurm_script_writer.py 32 v_m apx 0 12 1 0 0 08 1
python3 slurm_script_writer.py 32 v_m apx 0 12 1 0 0 16 1