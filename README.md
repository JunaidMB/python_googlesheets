# Connecting to Google Sheets with Python

This repo contains a script that allows a user to connect to GoogleSheets and update data with Python. 

The code is held in the `main.py` script. Before the Python can be run, there is some setup to do. The best walkthrough on how to do this can be found [here](https://erikrood.com/Posts/py_gsheets.html). 

## Setup 

Details and screenshots of the setup can be shown in the link above but the broad steps are listed below.

The Setup procedure is:

1. Create a service account and OAuth2 credentials from Google API Console.
2. Create JSON Credentials for the service account and save into the Python project - save this as `credentials.json`. 
3. Enable Google Sheets API from the Google API console.
4. Make a Google Sheet and give access to the service email account in order to allow Python to connect to and edit the Google Sheet.

## Useful Links

1. Service Account setup and hello world example: https://erikrood.com/Posts/py_gsheets.html

2. Pysheets package documentation: https://github.com/nithinmurali/pygsheets

3. Google Cloud Console: https://console.cloud.google.com