from functions import *
from sheets import SHEET_LIST

# Iterate through Google Sheets
for sheet_info in SHEET_LIST:
    processor = GSheetProcessor(googlesheet_id=sheet_info['id'], worksheet_info=sheet_info)
    processor.process_and_upload()
