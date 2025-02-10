#! /bin/bash
for file in v_*.sh; do sbatch $file; done