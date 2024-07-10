import os
import pandas as pd

# Directory containing the BLAST result files
directory = 'aablastout'

# List to hold dataframes
df_list = []

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith("_blast_result.tsv"):
        # Extract the species name from the first three letters of the filename
        species = filename[:3]
        
        # Read the CSV file into a DataFrame
        filepath = os.path.join(directory, filename)
        df = pd.read_csv(filepath, sep='\t', header=None)
        
        # Add a new column for the species name
        df.insert(0, 'species', species)
        
        # Append the DataFrame to the list
        df_list.append(df)

# Concatenate all DataFrames in the list
combined_df = pd.concat(df_list, ignore_index=True)

# Save the combined DataFrame to a new CSV file
combined_df.to_csv('combined_blast_results.csv', index=False, header=False)
