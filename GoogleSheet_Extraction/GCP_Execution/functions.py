import pandas as pd
import gspread
import datetime
from google.cloud import storage


class GSheetProcessor:
    def __init__(self, googlesheet_id, worksheet_info):
        self.googlesheet_id = googlesheet_id
        self.worksheet_info = worksheet_info
        self.client = gspread.service_account()

    def get_sheet_data(self, worksheet_name):
        """
        This function opens each Google Sheet using the ID, then renames the worksheets and columns to a dataframe.
        """
        try:
            spreadsheet = self.client.open_by_key(self.googlesheet_id)
            worksheet = spreadsheet.worksheet(worksheet_name)
            data = worksheet.get_all_values()
            df = pd.DataFrame(data[1:], columns=data[0])
            return df

        except Exception as e:
            raise Exception(f"Error retrieving data from worksheet {worksheet_name}: {e}")

    def rename_and_process(self, data, worksheet_name):
        """
        This function renames each worksheet and column specified, then returns the modified dataframe.
        """
        try:
            if worksheet_name in self.worksheet_info['worksheet_rename_mapping']:
                new_worksheet_name = self.worksheet_info['worksheet_rename_mapping'][worksheet_name]
                data.rename(columns={worksheet_name: new_worksheet_name}, inplace=True)

            for index, new_column_name in self.worksheet_info['column_rename_mapping'].items():
                if index < len(data.columns):
                    data.rename(columns={data.columns[index]: new_column_name}, inplace=True)

            print(f"Renaming completed for {new_worksheet_name}")
            return data

        except Exception as e:
            raise Exception(f"Error renaming and processing data for worksheet {worksheet_name}: {e}")

    def save_to_gcp_bucket(self, processed_data, worksheet_name):
        """
        This function authenticates your connection to GCP, renames the filename then saves to the specified bucket.
        """
        try:
            storage_client = storage.Client()
            bucket = storage_client.get_bucket(self.worksheet_info['bucket_name'])

            date_str = datetime.date.today().strftime("%Y-%m-%d")
            file_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

            file_name = f"{worksheet_name}_{file_time}.csv"
            csv_content = processed_data.to_csv(index=False)
            file_path = f"{self.worksheet_info['folder_root']}{date_str}/{file_name}"

            blob = bucket.blob(file_path)
            blob.upload_from_string(csv_content)
            print(f"{file_name} now uploaded")
            return file_path

        except Exception as e:
            raise Exception(f"Error saving data to GCP bucket for worksheet {worksheet_name}: {e}")

    def process_and_upload(self):
        for worksheet_name in self.worksheet_info['worksheets']:
            data = self.get_sheet_data(worksheet_name)
            processed_data = self.rename_and_process(data, worksheet_name)
            file_path = self.save_to_gcp_bucket(processed_data, worksheet_name)
            print(f"{worksheet_name} data saved to {file_path}")
