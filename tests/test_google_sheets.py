
# scripts/test_google_sheets_connection.py
from src.google_sheets import get_sheet_data

data = get_sheet_data()
if data:
    print("Data fetched successfully:", data)
else:
    print("Failed to fetch data.")
