#!/bin/bash

# Create an output file
output_file="lnL_values.txt"
> "$output_file"

# Find all directories and process each one
for dir in */; do
    # Find the output file starting with 'out' in the current directory
    output_file_in_dir=$(find "$dir" -maxdepth 1 -name 'out*' -type f)
    
    # Check if an output file was found
    if [ -n "$output_file_in_dir" ]; then
        # Extract the lnL value
        lnL_value=$(grep 'lnL' "$output_file_in_dir" | sed 's/..*\:\ *//;s/\ ..*//')
        
        # Append the directory name and lnL value to the output file
        echo "$dir $lnL_value" >> "$output_file"
    fi
done

echo "lnL values have been extracted to $output_file"

