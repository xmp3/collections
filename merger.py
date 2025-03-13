import os
import glob
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_folder")
parser.add_argument("output_filename")

args = parser.parse_args()
input_folder = args.input_folder
output_filename = args.output_filename

csv_files = glob.glob(os.path.join(input_folder, '*.csv'))
dataframes = [pd.read_csv(file) for file in csv_files]
merged_df = pd.concat(dataframes, ignore_index=True)
csv_output_path = os.path.join(input_folder, output_filename)
merged_df.to_csv(csv_output_path, index=False)

print(f"CSV files successfully merged into '{output_filename}'.")
