pip install numpy
pip install pandas

#!/usr/bin/env python
import numpy as np
import pandas as pd

def normalize_expression(data_matrix):
    """
    Normalize expression data by calculating the z-score for each gene across samples.
    """
    mean_values = np.mean(data_matrix, axis=1)
    std_devs = np.std(data_matrix, axis=1)
    normalized_matrix = (data_matrix - mean_values[:, np.newaxis]) / std_devs[:, np.newaxis]
    return normalized_matrix

def main():
    input_file = "expression_data.csv"
    output_file = "normalized_expression.csv"
    
    # Load expression data from CSV
    data = pd.read_csv(input_file, index_col=0)
    
    print("Normalizing expression data")
    normalized_data = normalize_expression(data.values)
    
    # Save normalized data to CSV
    normalized_df = pd.DataFrame(normalized_data, columns=data.columns, index=data.index)
    normalized_df.to_csv(output_file)
    
    print("Normalization completed. Normalized expression data saved as", output_file)

if __name__ == "__main__":
    main()
