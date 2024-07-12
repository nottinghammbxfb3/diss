# Supplementary material
## Tools used throughout:
- Python version 3.12.2
- Pandas version 2.2.2
## 1. Dataset construction
### A. Genome download
- NCBI Datasets version 16.13.0
- NCBI Datasets accession sourced from NCBI Datasets genome website: https://www.ncbi.nlm.nih.gov/datasets/genome/
- Example command ran in command line to download a genome (Homo sapiens):
  ```
  datasets download genome accession GCF_000001405.40 --include gff3,rna,cds,protein,genome,seq-report
  ```
### B. BUSCO genome quality control
- BUSCO version 5.4.7
- Lineage used: eukaryota_odb10
- Example script: [busco_example.sh](busco_example.sh)



__Table S1.1 Taxonomy, Busco missing percentage and NCBI datasets accession number.__ * indicates using a clade instead of kingdom. ([species.tsv](species.tsv))
|Genus|Species|Kingdom|Phylum|Class|Order|Family|Busco Missing (%)|NCBI Accession|
|-|-|-|-|-|-|-|-|-|
|Homo|sapiens|Animal|Chordata|Mammalia|Primates|Hominidae|0|GCF_000001405.40|
|Mus|musculus|Animal|Chordata|Mammalia|Rodentia|Muridae|0|GCF_000001635.27|
|Xenopus|laevis|Animal|Chordata|Amphibia|Anura|Pipidae|0.4|GCF_017654675.1|
|Schistosoma|haematobium|Animal|Platyhelminthes|Trematoda|Strigeidida| Schistosomatidae|6.3|GCF_000699445.3|
|Drosophila|melanogaster|Animal|Arthropoda|Insecta|Diptera| Drosophilidae|0|GCF_000001215.4|
|Caenorhabditis|elegans|Animal|Nematoda|Chromadorea|Rhabditida|Rhabditidae|2.8|GCF_000002985.6|
|Corticium |candelabrum|Animal|Porifera|Homoscleromorpha|Homosclerophorida|Plakinidae|1.9|GCF_963422355.1|
|Nematostella|vectensis|Animal|Cnidaria|Anthozoa|Actiniaria|Edwardsiidae|0|GCF_932526225.1|
|Crassostrea|virginica|Animal|Mollusca|Bivalvia|Ostreida|Ostreidae|0.8|GCF_002022765.2|
|Lytechinus| variegatus|Animal|Echinodermata|Echinoidea|Camarodonta|Toxopneustidae|0.8|GCF_018143015.1|
|Arabidopsis|thaliana|Plant|Streptophyta|Magnoliopsida|Brassicales|Brassicacae|0|GCF_000001735.4|
|Glycine|max|Plant|Streptophyta|Magnoliopsida|Fabales|Fabaceae|0|GCF_000004515.6|
|Oryza|sativa|Plant|Streptophyta|Magnoliopsida|Poales|Poacease|0|GCF_001433935.1|
|Solanum|stenotomum|Plant|Streptophyta|Magnoliopsida|Solanales|Solanaceae|0.8|GCF_019186545.1|
|Theobroma|cacao|Plant|Streptophyta|Magnoliopsida|Malvales|Malvaceae|0.4|GCF_000208745.1|
|Vitis|vinifera|Plant|Streptophyta|Magnoliopsida|Vitales|Vitaceae|0.3|GCF_030704535.1|
|Cyanidioschyzon|merolae|Plant|Rhodophyta|Bangiophyceae|Cyanidiales |Cyanidiaceae|20|GCF_000091205.1|
|Micromonas|commoda|Plant|Chlorophyta|Mamiellophyceae|Mamiellales|Mamiellaceae|9|GCF_000090985.2|
|Physcomitrella|patens|Plant|Bryophyta|Bryopsida|Funariales|Funariacaea|0.3|GCF_000002425.4|
|Marchantia|polymorpha|Plant|Hepatophyta|Marchantiopsida|Marchantiales|Marchantiaceae|0.4|GCA_037833965.1|
|Yarrowia|lipolytica|Fungi|Ascomycota|Saccharomycetes|Saccharomycetales|Dipodascaceae|1.5|GCF_014490615.1|
|Saccharomyces|cerevisiae|Fungi|Ascomycota|Saccharomycetes|Saccharomycetales|Saccharomycetaceae|5.5|GCF_000146045.2|
|Ustilaginoidea|virens|Fungi|Ascomycota|Sordariomycetes|Hypocreales|Clavicipitaceae|0.8|GCF_000687475.1|
|Schizosaccharomyces|osmophilus|Fungi|Ascomycota|Schizosaccharomycetes|Schizosaccharomycetales|Schizosaccharomycetaceae|2.3|GCF_027921745.1|
|Talaromyces|rugulosus|Fungi|Ascomycota|Eurotiomycetes|Eurotiales|Trichocomaceae|0.8|GCF_013368755.1|
|Geosiphon|pyriformis|Fungi|Glomeromycota|Glomeromycetes|Archaeosporales|Geosiphonaceae|7.4|GCA_016748015.1|
|Synchytrium|microbalum|Fungi|Chytridiomycota|Chytridiomycetes|Synchytriales|Synchytriaceae|3.9|GCF_006535985.1|
|Puccinia|triticina|Fungi|Basidiomycota|Pucciniomycetes|Pucciniales|Pucciniaceae|2.7|GCF_026914185.1|
|Kwoniella|botswanensis|Fungi|Basidiomycota|Tremellomycetes|Tremellales|Cryptococcaceae|2.4|GCF_036426115.1|
|Sporisorium|graminicola|Fungi|Basidiomycota|Ustilaginomycetes|Ustilaginales|Ustilaginaceae|0.4|GCF_005498985.1|
|Plasmodium|falciparum 3D7|Alveolata*|Apicomplexa|Aconoidasida|Haemosporida|Plasmodiidae|43.5|GCF_000002765.6|
|Tetrahymena|thermophila SB210|Alveolata*|Ciliophora|Oligohymenophorea|Hymenostomatida|Tetrahymenidae|38|GCF_000189635.1|
|Dictyostelium|discoideum AX4|Amoebozoa*|Evosea|Eumycetozoa| Dictyosteliales|Dictyosteliaceae|4.3|GCF_000004695.1|
|Giardia|intestinalis|Metamonada*|Fornicata|N/A|Diplomonadida|Hexamitidae|70.2|GCF_000002435.2|
|Leishmania|major strain Friedlin|Discoba*|Euglenozoa|Kinetoplastea| Trypanosomatida|Trypanosomatidae|36.9|GCF_000002725.2|



### C. BLAST search
- BLASTp with Homo sapiens eL22 amino acid sequence as the query, was ran on custom database with evalue threshold of 1e-7.
- All species amino acid genomes stored in a single directory, named by first 3 letters of genus.
- BLAST version 2.14.1 (Custom version for HPC: blast-uoneasy/2.14.1-gompi-2023a)
- Create BLAST custom database script: [make_blastdb.sh](make_blastdb.sh)
- Homo sapiens eL22 amino acid query sequence: [hs_el22.faa](hs_el22.faa)
- Run BLASTp on custom database script: [run_blast_aa.sh](run_blast_aa.sh)
- Extract BLAST results script: [get_blast_results.py](get_blast_results.py)
- Extract BLAST hit NCBI codes: [make_hits_file.py](make_hits_file.py)
- Extract BLAST hit sequences: [get_hits_seqs.py](get_hits_seqs.py)
- Some genes had multiple proteins appear in the BLAST result, these were manually filtered to include 1 protein per gene by selecting the longest protein for each gene.
- This was done by searching the protein codes in the given species .gff annotation file, and checking the 'GeneID' was unique relative to the other hits for that species.
- Out of 74 proteins, 63 were unique and included in downstream analysis.
- The pre-filtered amino acid sequences, with * indicating uniqueness and inclusion downstream: [all_hit_seqs.faa](all_hit_seqs.faa)

__Table S1.2 BLASTp results.__ Species name is represented by first 3 letters of genus. ([combined_blast_results.csv](combined_blast_results.csv))
|Species|Query sequence|Database sequence|Percent identity|Alignment length|Number of mismatches|Number of gap openings|Start of alignment in query|End of alignment in query|Start of alignment in subject|End of alignment in subject|Expectation value     |Bit score|
|-------|--------------|-----------------|----------------|----------------|--------------------|----------------------|---------------------------|-------------------------|-----------------------------|---------------------------|----------------------|---------|
|scz    |NP_000974.1   |XP_056037923.1   |52.778          |108             |49                  |1                     |20                         |125                      |11                           |118                        |8.180000000000001e-37 |119.0    |
|sac    |NP_000974.1   |NP_013162.1      |43.59           |117             |59                  |2                     |1                          |117                      |1                            |110                        |4.8e-19               |74.7     |
|sac    |NP_000974.1   |NP_116619.1      |42.735          |117             |60                  |2                     |1                          |117                      |1                            |110                        |5.18e-18              |72.0     |
|cya    |NP_000974.1   |XP_005538757.1   |58.095          |105             |44                  |0                     |14                         |118                      |12                           |116                        |2.1900000000000003e-31|106.0    |
|xen    |NP_000974.1   |NP_001081541.1   |92.437          |119             |9                   |0                     |1                          |119                      |1                            |119                        |3.91e-68              |202.0    |
|xen    |NP_000974.1   |XP_018081603.2   |92.437          |119             |9                   |0                     |1                          |119                      |42                           |160                        |9.189999999999999e-68 |203.0    |
|xen    |NP_000974.1   |NP_001091257.1   |73.913          |115             |29                  |1                     |13                         |127                      |10                           |123                        |7.43e-45              |143.0    |
|the    |NP_000974.1   |XP_007050938.2   |66.071          |112             |35                  |2                     |8                          |117                      |5                            |115                        |3.72e-34              |115.0    |
|the    |NP_000974.1   |XP_007035624.1   |73.196          |97              |23                  |2                     |21                         |115                      |19                           |114                        |1.71e-33              |113.0    |
|the    |NP_000974.1   |XP_007050935.2   |56.557          |122             |40                  |4                     |8                          |117                      |5                            |125                        |8.520000000000001e-31 |107.0    |
|nem    |NP_000974.1   |XP_001626833.2   |77.551          |98              |21                  |1                     |21                         |118                      |15                           |111                        |3.15e-41              |133.0    |
|yar    |NP_000974.1   |XP_002143093.1   |45.6            |125             |58                  |2                     |1                          |125                      |1                            |115                        |6.319999999999999e-23 |84.7     |
|gia    |NP_000974.1   |XP_001704458.2   |28.814          |118             |77                  |4                     |1                          |117                      |1                            |112                        |5.04e-09              |48.9     |
|tet    |NP_000974.1   |XP_001014258.3   |54.783          |115             |47                  |2                     |13                         |123                      |5                            |118                        |8.44e-26              |94.0     |
|syn    |NP_000974.1   |XP_031025581.1   |53.922          |102             |44                  |2                     |19                         |117                      |16                           |117                        |3.95e-35              |116.0    |
|puc    |NP_000974.1   |XP_053024850.1   |52.041          |98              |47                  |0                     |20                         |117                      |50                           |147                        |1.48e-34              |116.0    |
|geo    |NP_000974.1   |KAG9295949.1     |49.58           |119             |55                  |3                     |1                          |117                      |1                            |116                        |7.37e-37              |121.0    |
|sol    |NP_000974.1   |XP_049384226.1   |65.741          |108             |34                  |2                     |21                         |126                      |19                           |125                        |2.36e-34              |115.0    |
|sol    |NP_000974.1   |XP_049407276.1   |63.889          |108             |36                  |2                     |21                         |126                      |19                           |125                        |5.6e-34               |115.0    |
|sol    |NP_000974.1   |XP_049407275.1   |63.889          |108             |36                  |2                     |21                         |126                      |19                           |125                        |5.6e-34               |115.0    |
|sol    |NP_000974.1   |XP_049407274.1   |63.889          |108             |36                  |2                     |21                         |126                      |19                           |125                        |5.6e-34               |115.0    |
|sol    |NP_000974.1   |XP_049407272.1   |65.979          |97              |30                  |2                     |21                         |115                      |20                           |115                        |5.25e-30              |105.0    |
|lyt    |NP_000974.1   |XP_041479948.1   |82.524          |103             |17                  |1                     |17                         |119                      |21                           |122                        |7.9e-47               |148.0    |
|sch    |NP_000974.1   |XP_051067065.1   |55.455          |110             |45                  |3                     |10                         |117                      |13                           |120                        |6.760000000000001e-35 |116.0    |
|cae    |NP_000974.1   |NP_494932.1      |57.937          |126             |53                  |0                     |3                          |128                      |5                            |130                        |1.19e-47              |149.0    |
|mus    |NP_000974.1   |NP_033105.1      |99.219          |128             |1                   |0                     |1                          |128                      |1                            |128                        |9.41e-91              |259.0    |
|mus    |NP_000974.1   |NP_001264042.1   |99.194          |124             |1                   |0                     |5                          |128                      |28                           |151                        |1.11e-86              |250.0    |
|mus    |NP_000974.1   |NP_001264043.1   |98.75           |80              |1                   |0                     |1                          |80                       |1                            |80                         |5.27e-53              |163.0    |
|mus    |NP_000974.1   |NP_001334155.1   |70.312          |128             |31                  |2                     |1                          |128                      |1                            |121                        |9.82e-46              |145.0    |
|mus    |NP_000974.1   |NP_080793.1      |70.312          |128             |32                  |2                     |1                          |128                      |1                            |122                        |1.57e-45              |145.0    |
|cor    |NP_000974.1   |XP_062501865.1   |63.158          |114             |41                  |1                     |14                         |127                      |12                           |124                        |3.27e-51              |158.0    |
|dic    |NP_000974.1   |XP_636907.1      |53.226          |124             |50                  |3                     |1                          |124                      |1                            |116                        |1.17e-38              |125.0    |
|dic    |NP_000974.1   |XP_635911.1      |52.419          |124             |51                  |3                     |1                          |124                      |1                            |116                        |1.32e-37              |122.0    |
|cra    |NP_000974.1   |XP_022343312.1   |77.228          |101             |22                  |1                     |19                         |119                      |24                           |123                        |6.33e-56              |171.0    |
|mic    |NP_000974.1   |XP_002499883.1   |61.062          |113             |41                  |2                     |14                         |124                      |6                            |117                        |2.04e-44              |139.0    |
|spo    |NP_000974.1   |XP_029742903.1   |54.032          |124             |57                  |0                     |3                          |126                      |2                            |125                        |4.05e-44              |139.0    |
|ust    |NP_000974.1   |XP_043000912.1   |49.606          |127             |61                  |1                     |1                          |127                      |1                            |124                        |3.38e-38              |124.0    |
|phy    |NP_000974.1   |XP_024388974.1   |64.463          |121             |37                  |4                     |8                          |125                      |13                           |130                        |2.36e-46              |147.0    |
|phy    |NP_000974.1   |XP_024378492.1   |63.846          |130             |42                  |3                     |1                          |126                      |1                            |129                        |4.01e-39              |128.0    |
|phy    |NP_000974.1   |XP_024369030.1   |63.281          |128             |42                  |3                     |1                          |126                      |4                            |128                        |6.17e-38              |125.0    |
|phy    |NP_000974.1   |XP_024368971.1   |63.281          |128             |42                  |3                     |1                          |126                      |4                            |128                        |6.17e-38              |125.0    |
|phy    |NP_000974.1   |XP_024387983.1   |63.559          |118             |40                  |2                     |11                         |126                      |13                           |129                        |3.46e-36              |121.0    |
|phy    |NP_000974.1   |XP_024381496.1   |60.8            |125             |46                  |2                     |4                          |126                      |6                            |129                        |1.37e-35              |119.0    |
|phy    |NP_000974.1   |XP_024389419.1   |62.5            |128             |43                  |3                     |1                          |126                      |1                            |125                        |2.04e-31              |108.0    |
|hom    |NP_000974.1   |NP_000974.1      |100.0           |128             |0                   |0                     |1                          |128                      |1                            |128                        |3.0699999999999997e-91|261.0    |
|hom    |NP_000974.1   |NP_001307380.1   |70.312          |128             |31                  |2                     |1                          |128                      |1                            |121                        |1.88e-46              |148.0    |
|hom    |NP_000974.1   |NP_001093115.1   |70.312          |128             |32                  |2                     |1                          |128                      |1                            |122                        |2.6599999999999998e-46|147.0    |
|dro    |NP_000974.1   |NP_477134.1      |63.2            |125             |43                  |3                     |4                          |126                      |174                          |297                        |6.06e-38              |130.0    |
|dro    |NP_000974.1   |NP_611771.1      |47.788          |113             |55                  |3                     |8                          |117                      |179                          |290                        |9.88e-27              |101.0    |
|tal    |NP_000974.1   |XP_035349240.1   |48.031          |127             |62                  |1                     |1                          |127                      |1                            |123                        |2.66e-38              |124.0    |
|gly    |NP_000974.1   |NP_001236862.1   |65.0            |120             |39                  |2                     |9                          |126                      |1                            |119                        |7.64e-38              |125.0    |
|gly    |NP_000974.1   |NP_001236434.2   |65.0            |120             |39                  |2                     |9                          |126                      |1                            |119                        |9.83e-38              |125.0    |
|gly    |NP_000974.1   |NP_001336711.1   |63.559          |118             |40                  |2                     |11                         |126                      |8                            |124                        |1.44e-35              |119.0    |
|gly    |NP_000974.1   |XP_003556520.1   |62.712          |118             |41                  |2                     |11                         |126                      |8                            |124                        |3.73e-35              |118.0    |
|gly    |NP_000974.1   |XP_040868309.1   |66.667          |108             |33                  |2                     |21                         |126                      |19                           |125                        |1.66e-34              |117.0    |
|gly    |NP_000974.1   |XP_014626808.1   |66.667          |108             |33                  |2                     |21                         |126                      |19                           |125                        |1.66e-34              |117.0    |
|gly    |NP_000974.1   |NP_001237039.1   |66.667          |108             |33                  |2                     |21                         |126                      |18                           |124                        |1.9599999999999998e-34|116.0    |
|gly    |NP_000974.1   |NP_001234976.1   |65.741          |108             |34                  |2                     |21                         |126                      |19                           |125                        |8.53e-34              |115.0    |
|kwo    |NP_000974.1   |XP_064745982.1   |54.955          |111             |49                  |1                     |16                         |126                      |15                           |124                        |1.57e-39              |127.0    |
|mar    |NP_000974.1   |BFI32126.1       |56.923          |130             |51                  |3                     |1                          |126                      |1                            |129                        |3.93e-47              |147.0    |
|vit    |NP_000974.1   |XP_002268941.1   |69.444          |108             |30                  |2                     |21                         |126                      |19                           |125                        |1.0400000000000001e-36|122.0    |
|vit    |NP_000974.1   |XP_003633625.1   |70.37           |108             |29                  |2                     |21                         |126                      |18                           |124                        |3.17e-36              |120.0    |
|vit    |NP_000974.1   |XP_010659646.1   |69.444          |108             |30                  |2                     |21                         |126                      |18                           |124                        |3.17e-35              |118.0    |
|vit    |NP_000974.1   |XP_002269845.1   |66.972          |109             |33                  |2                     |11                         |117                      |8                            |115                        |4.31e-34              |115.0    |
|pla    |NP_000974.1   |XP_001349308.1   |50.0            |100             |49                  |1                     |19                         |118                      |40                           |138                        |3.77e-33              |111.0    |
|ory    |NP_000974.1   |XP_015630925.1   |64.865          |111             |35                  |3                     |19                         |126                      |22                           |131                        |4.8e-34               |115.0    |
|ory    |NP_000974.1   |XP_015647764.1   |64.865          |111             |35                  |3                     |19                         |126                      |21                           |130                        |2.1200000000000002e-33|114.0    |
|lei    |NP_000974.1   |XP_001687026.1   |44.34           |106             |54                  |3                     |21                         |123                      |26                           |129                        |3.11e-28              |99.4     |
|lei    |NP_000974.1   |XP_001686907.1   |44.34           |106             |54                  |3                     |21                         |123                      |26                           |129                        |3.11e-28              |99.4     |
|ara    |NP_000974.1   |NP_974229.1      |65.517          |116             |37                  |2                     |13                         |126                      |10                           |124                        |4.66e-36              |120.0    |
|ara    |NP_000974.1   |NP_187207.1      |65.517          |116             |37                  |2                     |13                         |126                      |10                           |124                        |4.66e-36              |120.0    |
|ara    |NP_000974.1   |NP_001078112.1   |65.517          |116             |37                  |2                     |13                         |126                      |10                           |124                        |4.66e-36              |120.0    |
|ara    |NP_000974.1   |NP_198129.1      |66.667          |99              |30                  |2                     |19                         |115                      |16                           |113                        |7.04e-30              |104.0    |
|ara    |NP_000974.1   |NP_171782.1      |56.154          |130             |52                  |4                     |1                          |128                      |1                            |127                        |1.78e-28              |101.0    |

## 2. Phylogenetic reconstruction of eL22 family.
### A. Multiple sequence alignment (MSA)
- MAFFT version 7.511
- Using web tool: https://mafft.cbrc.jp/alignment/server/index.html 
- Strategy: Auto (which selected L-INS-I)
- Alignment file: [aa_msa.aln](aa_msa.aln)

### B. Trimming MSA
- Trimal version 1.4.1
- Model used: gappyout
- Trimmed alignment file: [trim_aa_msa.aln](trim_aa_msa.aln)
- Command ran in command line:
  ```
  trimal -in aa_msa.aln -out trim_aa_msa.aln -gappyout
  ```
### C. IQTREE maximum likelihood phylogenetic reconstruction:
- IQTREE version 2.1.4-beta COVID-edition built Jun 24 2021
- Run IQTREE with ModelFinder Plus and 1000 bootstrap replicates: [run_iqtree.sh](run_iqtree.sh)
- Model selected by ModelFinder Plus: Q.yeast+G4
- IQTREE output file, including model selection and consensus tree: [iqtree_out.iqtree](iqtree_out.iqtree)

## 3. Gene tree reconciliation
### A. Installation
- GeneRax version 2.1.3
- Dependancies:
  - gcc_linux-64 version 9.3.0
  - gxx_linux-64 version 9.3.0
  - cmake version 3.18.4
  - openmpi version 4.0.5
  - Command ran to create conda environment with dependancies:
    ```
    conda create -n generax-env gcc_linux-64=9.3.0 gxx_linux-64=9.3.0 cmake=3.18.4 openmpi=4.0.5 -c conda-forge
    ```
### B. Input files
- Names of proteins and species were changed to run in GeneRax.
- Python dictionary to convert NCBI codes to species and gene names: [convert_protein_names.py](convert_protein_names.py)
- MSA in fasta format: [msa.fasta](msa.fasta)
- Species tree: [species.newick](species.newick)
- Gene tree: [gene_tree.newick](gene_tree.newick)
- Mapping file: [map.link](map.link)
- Family file: [family.txt](family.txt)
### C. Running GeneRax
- All input files stored in directory within GeneRax directory (created by GeneRax install) called gr_data.
- Settings:
  - To account for duplications and losses: --rec-model UndatedDL
  - To evaluate the likelihood, the duplication and loss rates, and the reconciliation of the starting gene tree: --strategy EVAL
  - Optimal substitution model identified by IQTREE: subst_model = Q.yeast+G4 (In family.txt)
- Commands run in command line from within GeneRax directory:
  ```
  conda activate generax-env
  ```
  ```
  build/bin/generax --families gr_data/family.txt --species-tree gr_data/species.newick --rec-model UndatedDL --prefix generax_out --strategy EVAL
  ```

