import pandas as pd
import numpy as np
import pygsheets
import os

# Pysheets documentation: https://github.com/nithinmurali/pygsheets

'''
Requirements:
1. Setup Google service account and follow the steps here: https://erikrood.com/Posts/py_gsheets.html
2. Enable Google Sheets API from the Google Cloud Platform.
3. Give Google Sheet access to the created Google service account email address: <name_here>-compute@developer.gserviceaccount.com via the Share button
'''

# Authorisation - Must have credentials from Google Service Account as JSON
gc = pygsheets.authorize(service_file = os.path.join(os.getcwd(), "credentials.json"))


# ADD NEW DATA TO GOOGLESHEETS
# Load Data
day1_data = pd.read_csv('./data/day1_data.csv')

# Post data to Google Sheet
## Open the Google Spreadsheet with the name 'PY to Gsheet Test'
sh = gc.open('PY to Gsheet Test')

## Select the worksheet within the Google Spreadsheet that we want to add data to
wks = sh[0] # Selects the first worksheet

## Update the first sheet with data, let the dataframe start at row 1 and column 1
sh[0].set_dataframe(day1_data, (1, 1))

# APPEND DATA TO AN EXISTING WORKSHEET WITH DATA
# Load Data
day2_data = pd.read_csv('./data/day2_data.csv')

# Post data to Google Sheet
## Append new rows to the table in the worksheet 1 - Take existing data as a dataframe
existing_data = sh[0].get_as_df()

## Union new data to existing data
new_data = pd.concat([existing_data, day2_data], axis = 0)

## Update the first sheet with data, this will overwrite the previous data
sh[0].set_dataframe(new_data, (1, 1))

