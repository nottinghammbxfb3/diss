#!/bin/bash

#SBATCH --partition=defq
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=50
#SBATCH --mem=100g
#SBATCH --time=10:00:00
#SBATCH --job-name=my_job
#SBATCH --output=/gpfs01/home/mbxfb3/slurm-%x-%j.out
#SBATCH --mail-type=ALL
#SBATCH --mail-user=mbxfb3@exmail.nottingham.ac.uk

source activate /home/mbxfb3/miniconda3/envs/iqtree
cd /home/mbxfb3/diss/iqtree

/home/mbxfb3/miniconda3/envs/iqtree/bin/iqtree2 -s trim_aa_msa.aln -m MFP -B 1000