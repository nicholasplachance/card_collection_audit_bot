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

        # Extract headers
        main_headers = [header.strip() for header in all_values[0]]
        sub_headers = [header.strip() for header in all_values[1]]
        data = all_values[2:]
        
        # Print headers and first few rows of data for debugging
        print("Main headers found:", main_headers)
        print("Sub headers found:", sub_headers)
        print("First few rows of data:", data[:5])

        # Define the required columns
        required_columns = ['Name', 'Set Number', 'Rarity', 'Have', 'Grade']
        
        # Dictionary to hold data for each set
        sets_data = {}
        
        # Iterate through the main headers to process each set
        current_col = 0
        while current_col < len(main_headers):
            # Get the name of the set
            set_name = main_headers[current_col]
            if not set_name or 'Set List' not in set_name:
                current_col += len(required_columns) + 1  # Skip to the next set
                continue
            
            # Determine the start and end indices for sub-headers and columns
            start_col = current_col
            end_col = start_col + len(required_columns)
            if end_col > len(sub_headers):
                end_col = len(sub_headers)
            
            # Extract sub-headers for this set
            set_sub_headers = sub_headers[start_col:end_col]
            
            # Find indices of required columns in the sub-headers
            column_indices = {col: set_sub_headers.index(col) for col in required_columns if col in set_sub_headers}
            
            # Print column indices for debugging
            print(f"Processing set: {set_name}")
            print("Column indices for this set:", column_indices)
            
            # If we have valid column indices, process the data
            if column_indices:
                set_data = []
                for row in data:
                    if len(row) > end_col:  # Check if row is long enough
                        set_entry = {
                            col: row[column_indices.get(col, -1)] if column_indices.get(col, -1) != -1 else None
                            for col in required_columns
                        }
                        # Remove entries where all fields are blank
                        if any(set_entry.values()):  # Keep entry if any value is non-empty
                            set_data.append(set_entry)
                
                sets_data[set_name] = set_data
                print(f"Processed data for {set_name}: {set_data[:5]}")  # Print first 5 entries for each set
            else:
                print(f"No valid column indices found for {set_name}")
            
            # Move to the next set
            current_col = end_col + 1
        
        if not sets_data:
            print("No data processed for any sets.")
        
        return sets_data
    
    except gspread.exceptions.GSpreadException as e:
        print(f"Error fetching sheet data: {e}")
        return None
