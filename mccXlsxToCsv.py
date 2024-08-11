#!/usr/bin/python

import pandas as pd
import argparse
import re

def expand_mcc_ranges(df):
    expanded_rows = []

    for index, row in df.iterrows():
        mcc = row['MCC']
        name = row['Name']

        # Check if MCC is like 'G300' and Name contains 'codes between XXXX and YYYY'
        if isinstance(mcc, str) and mcc.startswith('G') and 'codes between' in name:
            # Extract the range from the Name
            range_match = re.search(r'codes between (\d{4}) and (\d{4})', name)
            if range_match:
                start_code = int(range_match.group(1))
                end_code = int(range_match.group(2))
                clean_name = name.split('(')[0].strip()

                # Create rows for each MCC code in the range
                for code in range(start_code, end_code + 1):
                    expanded_rows.append({'MCC': code, 'Name': clean_name})
        else:
            # For non-range rows, convert MCC to int if possible
            try:
                mcc = int(mcc)
            except ValueError:
                pass
            expanded_rows.append({'MCC': mcc, 'Name': name})

    # Convert to DataFrame
    df_expanded = pd.DataFrame(expanded_rows)

    # Check for non-digit MCC codes
    non_digit_codes = df_expanded[df_expanded['MCC'].apply(lambda x: not str(x).isdigit())]

    # If non-digit codes found, show a warning
    if not non_digit_codes.empty:
        print("Warning: Non-digit MCC codes found and will be excluded:")
        print(non_digit_codes)

    # Keep only digit MCC codes
    df_expanded = df_expanded[df_expanded['MCC'].apply(lambda x: str(x).isdigit())]

    # Identify non-unique names
    name_counts = df_expanded['Name'].value_counts()
    non_unique_names = name_counts[name_counts > 1].index

    # Append MCC to names that are not unique
    df_expanded['Name'] = df_expanded.apply(
        lambda row: f"{row['Name']} ({row['MCC']})" if row['Name'] in non_unique_names else row['Name'],
        axis=1
    )

    # Sort by MCC column
    df_expanded.sort_values(by='MCC', inplace=True, ignore_index=True)

    return df_expanded

def excel_to_csv(input_file, output_file):
    # Read the Excel file
    df = pd.read_excel(input_file, sheet_name='Merchant Category Codes (MCC)', header=None, usecols=[2, 3], skiprows=4)

    # Rename the columns
    df.columns = ['MCC', 'Name']

    # Remove double quotes from 'Name' column
    df['Name'] = df['Name'].str.strip('"')

    # Expand MCC ranges, append MCC to Name only if necessary, and sort the list
    df_expanded = expand_mcc_ranges(df)

    # Save the extracted data to CSV
    df_expanded.to_csv(output_file, index=False, sep=';')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert specified columns from an Excel file to CSV with expanded and sorted MCC ranges.")
    parser.add_argument("-i", "--input", help="Input Excel file path", required=True)
    parser.add_argument("-o", "--output", help="Output CSV file path", required=True)
    args = parser.parse_args()

    excel_to_csv(args.input, args.output)
