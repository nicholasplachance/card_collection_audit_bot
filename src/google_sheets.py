import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config.settings import SPREADSHEET_ID, SHEET_NAME

def authenticate_google_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("config/credentials.json", scope)
    client = gspread.authorize(creds)
    return client

def get_sheet_data():
    client = authenticate_google_sheets()
    sheet = client.open_by_key(SPREADSHEET_ID).worksheet(SHEET_NAME)
    
    try:
        # Fetch all values from the sheet
        all_values = sheet.get_all_values()
        
        if not all_values:
            print("No data found.")
            return None

        # Extract headers and data
        main_headers = [header.strip() for header in all_values[0]]
        sub_headers = [header.strip() for header in all_values[1]]
        data = all_values[2:]

        # Print headers and first few rows of data for debugging
        print("Main headers found:", main_headers)
        print("Sub headers found:", sub_headers)

        # Define the required columns
        required_columns = ['Name', 'Set Number', 'Rarity', 'Have', 'Grade']
        
        # Dictionary to hold data for each set
        sets_data = {}

        # Process each column in the main header to find the sets
        current_col = 0

        while current_col < len(main_headers):
            set_name = main_headers[current_col]

            # If set_name does not include 'Set List', skip it
            if 'Set List' not in set_name:
                current_col += 1
                continue

            # Determine the end column for this set
            end_col = current_col + 1
            while end_col < len(main_headers) and main_headers[end_col] == "":
                end_col += 1

            # Extract sub-headers and find indices of required columns
            set_sub_headers = sub_headers[current_col:end_col]
            column_indices = {col: set_sub_headers.index(col) for col in required_columns if col in set_sub_headers}

            print(f"Processing set: {set_name}")
            print("Column indices for this set:", column_indices)

            if column_indices:
                set_data = []
                for row in data:
                    if len(row) > end_col:  # Ensure row is long enough
                        set_entry = {
                            col: row[column_indices.get(col, -1)] if column_indices.get(col, -1) != -1 else None
                            for col in required_columns
                        }
                        if any(set_entry.values()):  # Keep entry if any value is non-empty
                            set_data.append(set_entry)
                
                sets_data[set_name] = set_data
                print(f"Processed data for {set_name}: {set_data[:5]}")
            else:
                print(f"No valid column indices found for {set_name}")
            
            # Move to the next set
            current_col = end_col
        
        if not sets_data:
            print("No data processed for any sets.")
        
        return sets_data
    
    except gspread.exceptions.GSpreadException as e:
        print(f"Error fetching sheet data: {e}")
        return None
