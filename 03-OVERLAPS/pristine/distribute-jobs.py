import os
import sys
#from libra_py import CP2K_methods
import libra_py.packages.cp2k.methods as CP2K_methods 

run_slurm = False
submit_template = 'submit_template.pbs'
run_python_file = 'run_template.py'
istep = 1000
fstep = 1001
njobs = 1
submission_exe = 'qsub'
# Removing the previous folders if existed. You can keep them as well 
# but Libra will overwrite some of the data if their names are the same
os.system('rm -rf res job* all_logfiles all_pdosfiles all_images')

print('Distributing jobs...')
CP2K_methods.distribute_cp2k_libint_jobs(submit_template, run_python_file, istep, fstep, njobs, run_slurm, submission_exe)