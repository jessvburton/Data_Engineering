SHEET_LIST = [  # You can add more Google Sheets here, just keep the same formatting.
    {  # You can put the worksheet name here as a reminder
        'id': '', # This is the Google Sheet ID which can be found in the URL of the Google Sheet
        'worksheets': ['Original worksheet name 1', 'Original worksheet_name 4'], # Make sure the worksheets are in exactly the same format, from spacing to characters, otherwise it won't recognise them
        'worksheet_rename_mapping': { # This renaming will not rename the original worksheet names, but the copy you are creating
            'Original worksheet name 1': 'New worksheet name 1', 
            'Original worksheet name 4': 'New worksheet name 4'
        },
        'columns_to_extract': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        'column_rename_mapping': { # This renaming will not rename the original worksheet columns, but the copy you are creating
            0: 'Column 1', # This renamining works on column index position
            1: 'Column 2',
            2: 'Column 3',
            3: 'Column 4',
            4: 'Column 5',
            5: 'Column 6',
            6: 'Column 7',
            7: 'Column 8',
            8: 'Column 9',
            9: 'Column 10'
        },
        'empty_date_action': { # can be 'fill_with_default' or 'filter_out_empty_dates'
            3: 'fill_with_default',
            9: 'filter_out_empty_dates'
        },
        'date_format_columns': { # set the date format you want for columns
            'Original worksheet name 1': {
                3: '%Y-%m-%d',
                9: '%Y-%m-%d'
            },
            'Original worksheet name 4': {
                3: '%Y-%m-%d',
                9: '%Y-%m-%d'
            }
        },
        'bucket_name': 'data-analytics', # Example naming
        'folder_root': 'google-sheets-as-csvs/' # Example naming
    },
    {  # Here is a bank version
       # You can add as many worksheet names or columns as you wish. 
       # Keep repeating to add more Google Sheets, or to rename worksheets/columns differently for the same Google Sheet.
        'id': '',
        'worksheets': [", ""],
        'worksheet_rename_mapping': {
            "": "",
            "": "",
            "": "",
            "": ""
        },
        'columns_to_extract': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        'column_rename_mapping': {
            0: '',
            1: '',
            2: '',
            3: '',
            4: '',
            5: '',
            6: '',
            7: '',
            8: '',
            9: ''
        },
        'empty_date_action': {
            : '',
            : ''
        },
        'date_format_columns': {
            'Original worksheet name 1': {
                : '',
                : ''
            },
            'Original worksheet name 4': {
                : '',
                : ''
            }
        'bucket_name': '',
        'folder_root': ''
    }
]
