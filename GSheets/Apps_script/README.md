# Google Sheets Export and Modify Script

This Google Apps Script exports specified sheets from a Google Sheets spreadsheet to CSV files, modifying them by deleting specified columns, without altering the original sheets. The CSV files are saved in a Google Drive folder, organized by date.

## Prerequisites

* A Google Sheets spreadsheet with the sheets you want to export.
* A Google Drive folder where you want to save the exported CSV files.
* Basic understanding of Google Apps Script.

## Setup

1.  **Open the Script Editor:**
    * Open your Google Sheets spreadsheet.
    * Go to "Extensions" > "Apps Script".
2.  **Copy and Paste the Code:**
    * Delete any existing code in the script editor.
    * Copy and paste the provided JavaScript code into the script editor.
3.  **Replace `YOUR_FOLDER_ID`:**
    * In the line `const rootFolder = DriveApp.getFolderById('YOUR_FOLDER_ID');`, replace `'YOUR_FOLDER_ID'` with the actual ID of the Google Drive folder where you want to save the CSV files. To get the folder id, open the desired google drive folder, and the id will be in the url.
4.  **Define Sheets and Columns to Delete:**
    * Modify the `columnsToDeleteMap` object to specify the sheets you want to process and the columns you want to delete from each sheet.
        * The keys of the object are the sheet names (e.g., `"SHEET_NAME1"`).
        * The values are arrays of column indexes (0-based). For example, `[0, 2, 4]` means delete the first, third, and fifth columns.
        * Example:
            ```javascript
            var columnsToDeleteMap = {
                "DataSheet1": [0, 3], // Delete the first and fourth columns from 'DataSheet1'
                "ReportSheet": [1, 2, 5] // Delete the second, third, and sixth columns from 'ReportSheet'
            };
            ```
5.  **Save the Script:**
    * Click the save icon (disk icon) in the script editor.
    * Give your script a name.
6.  **Authorize the Script:**
    * When you run the script for the first time, you will be prompted to authorize it to access your Google Sheets and Google Drive.

## Usage

1.  **Run the Script:**
    * In the script editor, select the `exportAndModifySheetsWithoutAlteringOriginals` function from the function dropdown.
    * Click the "Run" button (play icon).
2.  **Check Google Drive:**
    * The script will create a folder in your specified Google Drive folder, named after the current date (YYYYMMDD).
    * Inside this folder, you will find the exported CSV files, named with the date and time, and the sheet name (e.g., `20231027_153000_DataSheet1.csv`).

## Script Description

The script performs the following actions:

* Iterates through the sheets defined in the `columnsToDeleteMap`.
* Creates a temporary copy of each sheet to avoid modifying the original data.
* Deletes the specified columns from the temporary sheet.
* Exports the modified data from the temporary sheet to a CSV string.
* Creates a folder (if it doesn't already exist) in the specified Google Drive location, named after the current date.
* Creates a new csv file in the date folder, with a date and time stamp, and the name of the sheet.
* Deletes the temporary sheet.
* Logs an error if a specified sheet is not found.

## Important Notes

* Ensure that the sheet names in `columnsToDeleteMap` match the actual sheet names in your spreadsheet.
* Column indexes are 0-based (the first column is 0, the second is 1, and so on).
* The script creates a new folder for each day the script is run. This will prevent files from being overwritten.
* The script adds a time stamp to the file name, in order to prevent files from being overwritten in the same day.
* The script surrounds cell values with double quotes (`"`) to ensure proper CSV formatting.
* If you have very large sheets, the script may take a long time to run.
