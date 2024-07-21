# src/google_sheets.py
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config.settings import SPREADSHEET_ID, SHEET_NAME

def authenticate_google_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("config/credentials.json", scope)
    client = gspread.authorize(creds)
    return client

def get_sheet_data():
    try:
        client = authenticate_google_sheets()
        sheet = client.open_by_key(SPREADSHEET_ID).worksheet(SHEET_NAME)
        data = sheet.get_all_records()
        print(f"Successfully fetched data from sheet: {SHEET_NAME}")
        return data
    except Exception as e:
        print(f"Error fetching data from Google Sheets: {e}")
        return None

def update_sheet_data(data):
    try:
        client = authenticate_google_sheets()
        sheet = client.open_by_key(SPREADSHEET_ID).worksheet(SHEET_NAME)
        sheet.update([data[0].keys()] + [list(item.values()) for item in data])
        print(f"Successfully updated sheet: {SHEET_NAME}")
    except Exception as e:
        print(f"Error updating Google Sheets: {e}")
