import glob
import os
import warnings
import pandas as pd

print("Which folder would you like to read from?")
path = input("Enter folder name: ")
file_type = input("Please provide the file type, ie 'csv' / 'txt' ...: ")
files = glob.glob(os.path.join(path, "*." + file_type))  # joins all files in the named folder

output_name = input("Enter the name for the output file generated:")

warnings.filterwarnings("ignore")

for f in files:
    if file_type == 'txt':  # use this one for .txt files
        df = pd.read_csv(f, sep='\t')
    elif file_type == 'csv':  # use this one for .csv files
        df = pd.read_csv(f, sep=',')
    else:
        df = pd.read_csv(f)

    print('Processing file:', f.split("\\")[-1])
    df.to_csv(output_name + '.csv')

print(f"{output_name}.csv has been saved to {path}")
