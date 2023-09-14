from functions import *
from sheets import SHEET_LIST

# Iterate through Google Sheets
for googlesheet_info in SHEET_LIST:
    googlesheet_id = googlesheet_info['id']
    worksheet_rename_mapping = googlesheet_info['worksheet_rename_mapping']
    column_rename_mapping = googlesheet_info['column_rename_mapping']
    bucket_name = googlesheet_info['bucket_name']
    folder_root = googlesheet_info['folder_root']

    for worksheet_name in googlesheet_info['worksheets']:
        # Retrieve data from Google Sheet
        data = get_sheet_data(googlesheet_id, worksheet_name)

        # Rename and process data
        processed_data = rename_and_process(data, worksheet_name, worksheet_rename_mapping, column_rename_mapping)

        # Save processed data to GCP bucket
        save_to_gcp_bucket(processed_data, worksheet_name, bucket_name, folder_root)
