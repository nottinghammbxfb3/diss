#!/bin/bash

#SBATCH --partition=defq
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=50
#SBATCH --mem=200g
#SBATCH --time=10:00:00
#SBATCH --job-name=my_job
#SBATCH --output=/gpfs01/home/mbxfb3/slurm-%x-%j.out
#SBATCH --mail-type=ALL
#SBATCH --mail-user=mbxfb3@exmail.nottingham.ac.uk

export NUMEXPR_MAX_THREADS=50
cd /home/mbxfb3/diss/animal
module load  busco-uoneasy/5.4.7-foss-2023a
busco -i genomes/ -m genome -l eukaryota_odb10 -o busco_animal -c 50