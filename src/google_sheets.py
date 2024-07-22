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
        all_values = sheet.get_all_values()
        
        if not all_values:
            print("No data found.")
            return None

        main_headers = [header.strip() for header in all_values[0]]
        sub_headers = [header.strip() for header in all_values[1]]
        data = all_values[2:]

        required_columns = ['Name', 'Set Number', 'Rarity', 'Have', 'Grade']
        
        sets_data = {}
        current_col = 0

        while current_col < len(main_headers):
            set_name = main_headers[current_col]

            if 'Set List' not in set_name:
                current_col += 1
                continue

            end_col = current_col + 1
            while end_col < len(main_headers) and main_headers[end_col] == "":
                end_col += 1

            set_sub_headers = sub_headers[current_col:end_col]
            column_indices = {col: set_sub_headers.index(col) for col in required_columns if col in set_sub_headers}

            if column_indices:
                set_data = []
                for row in data:
                    if len(row) > end_col:
                        set_entry = {
                            col: row[column_indices.get(col, -1) + current_col] if column_indices.get(col, -1) != -1 else None
                            for col in required_columns
                        }
                        if any(set_entry.values()):
                            set_data.append(set_entry)
                
                sets_data[set_name] = set_data
            current_col = end_col
        
        return sets_data
    
    except gspread.exceptions.GSpreadException as e:
        print(f"Error fetching sheet data: {e}")
        return None

def get_set_data(set_name=None):
    all_data = get_sheet_data()
    if not all_data:
        return None
    
    if set_name:
        if set_name in all_data:
            return {set_name: all_data[set_name]}
        else:
            print(f"Set '{set_name}' not found.")
            return None
    else:
        return all_data

# Example usage
if __name__ == "__main__":
    set_name = input("Enter the set name you want to fetch (leave blank to fetch all sets): ")
    set_name = set_name.strip() if set_name else None

    data = get_set_data(set_name)
    
    if data:
        for set_name, set_data in data.items():
            print(f"\nData for set: {set_name}")
            for card in set_data:
                print(card)
    else:
        print("Failed to fetch data.")
