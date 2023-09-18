from functions import *
from sheets import SHEET_LIST

# Iterate through Google Sheets
for sheet_info in SHEET_LIST:
    processor = GSheetProcessor(sheet_info['id'], sheet_info)
    processor.process_and_upload()
