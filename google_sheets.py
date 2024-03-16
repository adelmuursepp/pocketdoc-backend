from dotenv import load_dotenv
import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

load_dotenv()

# Google sheets API setup
SERVICE_ACCOUNT_FILE = 'hacktheglobe24-b916c1161289.json'
SHEET_ID=os.environ['SHEET_ID']
RANGE_NAME = 'Sheet1!A1:E100'

# Just a helper function to get the data from google sheet
def read_google_sheet():
    # Authenticate and construct service
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=['https://www.googleapis.com/auth/spreadsheets'])
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SHEET_ID, range=RANGE_NAME).execute()
    values = result.get('values', [])
    # print(values)

    if not values:
        return 'No data found.'
    else:
        return values