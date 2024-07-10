#!/bin/bash

genome_dir="allaas"

for genome_file in ${genome_dir}/*.faa; do
    makeblastdb -in ${genome_file} -dbtype prot -out ${genome_dir}/${genome_file}
done