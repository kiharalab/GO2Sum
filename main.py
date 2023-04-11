import argparse
import os
import pandas as pd
from codes.model import function, subunit, pathway

if __name__ == '__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Run GO2Sum')
    parser.add_argument('--input_file', help='Tab-separated file with Protein ID and GO Annotation list')
    parser.add_argument('--summary_type', help='Type of summary to generate (function, subunit, pathway, or all)')
    parser.add_argument('--output_file', help='Name of result file')
    args = parser.parse_args()

    # Check if file argument is not empty
    if args.input_file:
        # Check if output file argument is provided, otherwise use default
        output_file = args.output_file or 'result.tab'
        try:
            # Read input file into a DataFrame
            df = pd.read_csv(args.input_file, sep='\t')
            # Generate the specified summary
            if args.summary_type == 'function':
                function(df, output_file)
            elif args.summary_type == 'subunit':
                subunit(df, output_file)
            elif args.summary_type == 'pathway':
                pathway(df, output_file)
            elif args.summary_type == 'all':
                function(df, output_file)
                subunit(df, output_file)
                pathway(df, output_file)
            else:
                print(f"Error: '{args.summary_type}' is not a valid summary type. Please choose from 'function', 'subunit', 'pathway' or 'all'.")
        except FileNotFoundError:
            # Handle file not found error
            file_name = os.path.basename(args.input_file)
            print(f"Error: file '{file_name}' not found. Please check that the file exists and that you have permission to read it.")
    else:
        print("Error: file name is empty. Please provide the name of a tab-separated file with Protein ID and GO Annotation list.")
