import pandas as pd

# Read the input file (assuming it's comma-separated as .csv format)
df = pd.read_csv('combined_blast_results.csv', header=None)

# Extract the third column (index 2, as pandas uses 0-based indexing)
database_sequences = df.iloc[:, 2]

# Save the extracted column to a new .txt file
database_sequences.to_csv('hits_seqs.txt', index=False, header=False)
