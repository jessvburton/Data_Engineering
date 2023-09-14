import pandas as pd
import gspread
import datetime
from google.cloud import storage
from googleapiclient._auth import default_credentials


def get_sheet_data(googlesheet_id, worksheet_name):
    # Authenticates the connection to the API using service account credentials.
    # Google Sheets API v4 - https://developers.google.com/identity/protocols/oauth2/scopes#sheets
    scope = ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive']
    credentials = default_credentials(scopes=scope)
    client = gspread.authorize(credentials)  # https://docs.gspread.org/en/latest/oauth2.html

    # Goes through each spreadsheet/worksheet to save them as a data frame
    try:
        # Open spreadsheet using ID
        spreadsheet = client.open_by_key(googlesheet_id)

        # Select worksheet by its name
        worksheet = spreadsheet.worksheet(worksheet_name)

        # Get all values
        data = worksheet.get_all_values()

        # Convert to df
        df = pd.DataFrame(data[1:], columns=data[0])

        return df

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def rename_and_process(data, worksheet_name, worksheet_rename_mapping, column_rename_mapping):
    # Rename worksheet
    if worksheet_name in worksheet_rename_mapping:
        new_worksheet_name = worksheet_rename_mapping[worksheet_name]
        data.rename(columns={worksheet_name: new_worksheet_name}, inplace=True)

    # Rename columns
    for index, new_column_name in column_rename_mapping.items():
        if index < len(data.columns):
            data.rename(columns={data.columns[index]: new_column_name}, inplace=True)
          
    # Return the modified df
    print(f"Renaming completed for {new_worksheet_name}")
    return data


def save_to_gcp_bucket(processed_data, worksheet_name, bucket_name, folder_root):
    # Save df as csv in specified bucket
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)

    date_str = datetime.date.today().strftime("%Y-%m-%d")
    file_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

    file_name = f"{worksheet_name}_{file_time}.csv"
    csv_content = processed_data.to_csv(index=False)
    file_path = folder_root + date_str + "/" + file_name

    blob = bucket.blob(file_path)
    blob.upload_from_string(csv_content)

    print(f"{file_name} now uploaded to {folder_root}")
