import pandas as pd
import datacompy
import warnings

print("Enter the file names to compare.")
file1 = input("Enter name for file1: ")
file2 = input("Enter name for file2: ")
print("File1: ", file1)
print("File2: ", file2)

df1 = pd.read_csv(file1, sep='|')
df2 = pd.read_csv(file2, sep='|')

file_pk = input("Enter the primary key to join the two files on:")
print("file_pk: ", file_pk)

join_columns = file_pk.replace(' ', '').split("|")

output_name = input("Enter the name for the output file generated:")

warnings.filterwarnings("ignore")
compare = datacompy.Compare(df1=df1, df2=df2, join_columns=join_columns, df1_name=file1, df2_name=file2)
is_match = compare.matches(ignore_extra_columns=False)
print("Data Frames match? " + str(is_match) + "\n")


if not is_match:
    with open(output_name + ".txt", 'w') as f:
        f.write(compare.report())
print(compare.report())
