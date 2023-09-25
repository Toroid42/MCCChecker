#!/usr/bin/python

import pandas as pd
import argparse

def excel_to_csv(input_file, output_file):
    # Read the Excel file
    df = pd.read_excel(input_file, sheet_name='Merchant Category Codes (MCC)', header=None, usecols=[2, 3], skiprows=4)

    # Rename the columns
    df.columns = ['MCC', 'Name']
    
    # Remove double quotes from 'Name' column
    df['Name'] = df['Name'].str.strip('"')

    # Save the extracted data to CSV
    df.to_csv(output_file, index=False, sep=';')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert specified columns from an Excel file to CSV.")
    parser.add_argument("-i", "--input", help="Input Excel file path", required=True)
    parser.add_argument("-o", "--output", help="Output CSV file path", required=True)
    args = parser.parse_args()

    excel_to_csv(args.input, args.output)
