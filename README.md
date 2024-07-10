# Supplementary material
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
- Example script: [Busco_example.sh](busco_example.sh)



__Table S1.1 Taxonomy, Busco missing percentage and NCBI datasets accession number.__ * indicates using a clade instead of kingdom.
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
