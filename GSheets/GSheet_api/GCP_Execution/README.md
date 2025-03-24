# main.py
This function iterates through the data provided in sheets.py before calling on the functions in functions.py.

# functions.py
### get_sheet_data(googlesheet_id, worksheet_name)
1. This function authenticates your connection to Google Sheets API v4,
2. Opens each Google Sheet using the 'id' provided in sheets.py,
3. Selects each worksheet using 'worksheets' provided in sheets.py,
4. Takes all the values,
5. Inputs them to a dataframe

### def rename_and_process(data, worksheet_name, worksheet_rename_mapping, column_rename_mapping)
1. This function renames each worksheet in the dataframe using 'worksheet_rename_mapping' provided in sheets.py,
2. Renames each column in the dataframe using 'column_rename_mapping' provided in sheets.py,
3. Returns the modified dataframe

### def save_to_gcp_bucket(processed_data, worksheet_name, bucket_name, folder_root)
1. This function authenticates your connection to GCP,
2. Renames the filename based on the new worksheet names and the date/time,
3. Saves to the specified bucket/folder using 'bucket_name' and 'folder_root' provided in sheets.py

# sheets.py
You can repeat this structure as many times as you wish for different worksheets in the same Google Sheet or for a number of different Google Sheets.
One thing you will need to do is to make sure that your GCP Service Account has been granted editor permissions in the Google Sheet, otherwise you will encounter errors and the script will fail.
- id
- worksheets
- worksheet_rename_mapping
- column_rename_mapping
- bucket_name
- folder_root

**id:** The ID is the Google Sheet ID which you can find in the URL when you have the Google Sheet open.

**worksheets:** These are the worksheet names in the Google Sheet which you would like to take, rename and save as a CSV. Make sure you copy the worksheet name exactly otherwise it will not recognise it.

**worksheet_rename_mapping:** Here you will need to input the current worksheet name and what you would like it to be renamed to in the CSV. This renaming will not alter the original Google Sheet as the renaming takes place in a dataframe, before being saved as a CSV.

**column_rename_mapping:** Here the renaming is done by index position rather than current column names. This way you can see both methods and customise the code to what suits your requirements best. Again, this renaming will not alter the original Google Sheet as the renaming takes place in a dataframe, before being saved as a CSV.

**bucket_name:** The bucket in GCP you want.

**folder_root:** The folder in the bucket you wish to save the CSV to.

# Useful Links
- Google Sheets API v4 - https://developers.google.com/identity/protocols/oauth2/scopes#sheets
- https://docs.gspread.org/en/latest/oauth2.html
- https://oauth2client.readthedocs.io/en/latest/source/oauth2client.service_account.html
