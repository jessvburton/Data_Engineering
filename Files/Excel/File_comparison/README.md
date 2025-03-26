# Data Comparison Script using datacompy

This script compares two CSV files using the `datacompy` library and generates a report detailing the differences.

## Prerequisites

1.  **Python 3.x:** Ensure you have Python 3.x installed.
2.  **`pandas` and `datacompy` Libraries:** Install the libraries using pip:

    ```bash
    pip install pandas datacompy
    ```

## Setup

1.  **CSV Files:** Ensure the two CSV files you want to compare are in the same directory as the script, or provide the full file paths.
2.  **Delimiter:** The script assumes the CSV files use a pipe (`|`) as the delimiter. If your files use a different delimiter (e.g., comma, tab), you will need to modify the `sep` parameter in the `pd.read_csv()` calls.

## Usage

1.  Run the script:

    ```bash
    python your_script_name.py
    ```

2.  The script will prompt you to enter the names of the two files you want to compare. Enter the filenames (including extensions, e.g., `file1.csv`).
3.  The script will then prompt you to enter the primary key(s) to join the two files on. If there are multiple primary keys, enter them separated by a pipe (`|`). For example, `id|date`.
4.  Finally, the script will prompt you to enter the name for the output report file.
5.  The script will compare the two files using `datacompy` and print whether the data frames match.
6.  If the data frames do not match, the script will generate a detailed report of the differences and save it to a text file with the name you provided (e.g., `output_report.txt`). The report will also be printed to the console.
