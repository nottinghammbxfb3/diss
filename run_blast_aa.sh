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


cd /home/mbxfb3/diss/blast/
module load  blast-uoneasy/2.14.1-gompi-2023a

protein="hs_el22.faa"

genome_dir="allaas"

output_dir="aablastout"

mkdir -p "$output_dir"

for genome_file in ${genome_dir}/*.faa; do
    
    genome_name=$(basename ${genome_file} .faa)

    output_file="${genome_name}_blast_result.tsv"

    blastp -query ${protein} -db ${genome_file} -evalue 1e-7 -num_threads 32 -out ${output_dir}/${output_file} -outfmt 6
done
