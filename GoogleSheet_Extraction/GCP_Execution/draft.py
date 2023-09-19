import pandas as pd
import gspread
import datetime
from google.cloud import storage
from oauth2client.service_account import ServiceAccountCredentials
import os
from configs.sheets import ROC


class GSheetProcessor:
    def __init__(self, googlesheet_id, worksheet_info):
        self.googlesheet_id = googlesheet_id
        self.worksheet_info = worksheet_info

    def get_sheet_data(self, worksheet_name, columns_to_extract=None):
        """
        This function authenticates the connection to the API using a credentials file.
        Opens each Google Sheet using the ID, then renames the worksheets and columns to a dataframe.
        """
        scope = ['https://www.googleapis.com/auth/spreadsheets',
                 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('', scope)
        client = gspread.authorize(credentials)

        # Goes through each spreadsheet/worksheet to save them as a data frame
        try:
            spreadsheet = client.open_by_key(self.googlesheet_id)
            worksheet = spreadsheet.worksheet(worksheet_name)

            if columns_to_extract is None:
                data = worksheet.get_all_values()
                df = pd.DataFrame(data[1:], columns=data[0])
            else:
                col_letters = [chr(ord("A") + col_index) for col_index in columns_to_extract]
                col_range = ":".join(col_letters)
                data = worksheet.get(f"A1:{col_range}{worksheet.row_count}")
                df = pd.DataFrame(data, columns=col_letters)
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

    def convert_date_format(self, data, columns_to_change, new_date_formats):
        """
        Change the date format for specific columns in the dataframe
        """
        try:
            for column_index, new_date_format in zip(columns_to_change, new_date_formats):
                if 0 <= column_index < len(data.columns):
                    column_name = data.columns[column_index]
                    data[column_name] = pd.to_datetime(data[column_name], errors='coerce', dayfirst=True)
                    data[column_name] = data[column_name].dt.strftime(new_date_format)

            return data
        except Exception as e:
            raise Exception(f"Error changing date format for columns: {e}")

    def fill_empty_dates_with_default(self, data, column_indices):
        for idx in column_indices:
            col_name = data.columns[idx]
            if pd.api.types.is_datetime64_any_dtype(data[col_name]):
                data.loc[:, col_name].fillna(pd.to_datetime('1900-01-01'), inplace=True)
            else:
                data[col_name] = pd.to_datetime(data[col_name], errors='coerce')
                data.loc[:, col_name].fillna(pd.to_datetime('1900-01-01'), inplace=True)

        return data

    def filter_out_empty_dates(self, data, column_indices):
        for idx in column_indices:
            col_name = data.columns[idx]
            if pd.api.types.is_datetime64_any_dtype(data[col_name]):
                data = data.loc[~data[col_name].isnull()]
            else:
                data[col_name] = pd.to_datetime(data[col_name], errors='coerce')
                data = data.loc[~data[col_name].isnull()]

        return data

    def save_to_folder(self, processed_data, worksheet_name):
        file_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        current_folder = os.path.dirname(os.path.abspath(__file__))
        csv_file_path = os.path.join(current_folder, f'{worksheet_name}_{file_time}.csv')
        processed_data.to_csv(csv_file_path, index=False)

    def process_and_upload(self):
        for sheet_info in SHEET_LIST:
            worksheet_name = sheet_info['worksheets']
            columns_to_extract = sheet_info.get('columns_to_extract', None)
            data = self.get_sheet_data(worksheet_name, columns_to_extract)
            processed_data = self.rename_and_process(data, worksheet_name)

            date_format_columns = self.worksheet_info.get('date_format_columns', {}).get(worksheet_name, {})
            if date_format_columns:
                column_indices = list(date_format_columns.keys())
                date_formats = list(date_format_columns.values())
                print(f"columns to change format for {worksheet_name}: {column_indices}")
                print(f"date formats for {worksheet_name}: {date_formats}")
                # filter out empty dates
                processed_data = self.filter_out_empty_dates(processed_data, column_indices)
                # apply date format change
                processed_data = self.convert_date_format(processed_data, column_indices, date_formats)
                # fill empty date fields
                processed_data = self.fill_empty_dates_with_default(processed_data, column_indices)

            print(f"processed data for {worksheet_name}:\n{processed_data.head()}")

            self.save_to_folder(processed_data, worksheet_name)
            print(f"{worksheet_name} data saved")
