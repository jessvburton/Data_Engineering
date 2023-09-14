import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import os

"""
This script will download all sheets from the Google Sheet of your choice. 
You will need the spreadsheet id and to grant the Service Account editor access to the sheet.
"""

# Google Sheets API v4 - https://developers.google.com/identity/protocols/oauth2/scopes#sheets
scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']

# Credentials and authentication using the credentials file
credentials_file = ''  # TODO: Make sure the json file is saved locally and add the file name/path here
credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
client = gspread.authorize(credentials) 

original_spreadsheet_id = ''  # TODO: Add spreadsheet id found in the Google Sheet URL
original_spreadsheet = client.open_by_key(original_spreadsheet_id) 

# File timestamp
date_str = datetime.date.today().strftime("%Y-%m-%d")

for worksheet in original_spreadsheet.worksheets():
    worksheet_name = worksheet.title
    data = worksheet.get_all_values()
    df = pd.DataFrame(data[1:], columns=data[0])

    current_folder = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(current_folder, f'{worksheet_name}_{date_str}.csv')

    df.to_csv(csv_file_path, index=False)
