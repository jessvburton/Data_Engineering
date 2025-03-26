# CSV/TXT File Concatenation Script

This script concatenates multiple CSV or TXT files from a specified folder into a single CSV output file using the `pandas` library.

## Prerequisites

1.  **Python 3.x:** Ensure you have Python 3.x installed.
2.  **`pandas` Library:** Install the library using pip:

    ```bash
    pip install pandas
    ```

## Setup

1.  **Input Folder:** Ensure the folder containing the CSV or TXT files exists.
2.  **File Type:** The script supports CSV and TXT files.

## Usage

1.  Run the script:

    ```bash
    python your_script_name.py
    ```

2.  The script will prompt you to enter the name of the folder containing the files you want to concatenate.
3.  The script will then prompt you to enter the file type (either `csv` or `txt`).
4.  Finally, the script will prompt you to enter the name for the output CSV file.
5.  The script will read each file in the specified folder, concatenate them into a single pandas DataFrame, and save the result to a CSV file with the provided output name.
6.  The script will print the name of each processed file and a confirmation message when the output file is saved.
