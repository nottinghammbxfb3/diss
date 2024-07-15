#!/bin/bash

#SBATCH --partition=defq
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=16g
#SBATCH --time=10:00:00
#SBATCH --job-name=my_job
#SBATCH --output=/gpfs01/home/mbxfb3/slurm-%x-%j.out
#SBATCH --mail-type=ALL
#SBATCH --mail-user=mbxfb3@exmail.nottingham.ac.uk


cd /home/mbxfb3/diss/paml_data/branchsite/hs

codeml control.ctl