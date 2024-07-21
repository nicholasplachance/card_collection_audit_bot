import sys
import os

# Add the root directory of the project to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.google_sheets import get_sheet_data

def test_google_sheets_connection():
    data = get_sheet_data()
    output = ""
    
    # Prepare the output based on the data fetched
    if data:
        output += f"Data fetched successfully:\n"
        for set_name, entries in data.items():
            output += f"\n{set_name}:\n"
            for entry in entries:
                output += f"{entry}\n"
    else:
        output = "Failed to fetch data."
    
    # Write output to a file with UTF-8 encoding
    try:
        with open("output.txt", "w", encoding="utf-8") as file:
            file.write(output)
        print("Output written to output.txt")
    except Exception as e:
        print(f"Failed to write output: {e}")

if __name__ == "__main__":
    test_google_sheets_connection()
