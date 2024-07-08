# Supplementary material
## 1. Dataset construction
### A. Genome download
- NCBI Datasets version 16.13.0
- To download a dataset (Homo sapiens)
- datasets download genome accession GCF_000001405.40 --include gff3,rna,cds,protein,genome,seq-report
### B. Busco genome 
- Busco version 5.4.7
- busco -i genomes/ -m genome -l eukaryota_odb10 -o busco_animal -c 50
