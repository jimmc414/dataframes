import sys
import pandas as pd

def load_excel_files(file_paths):
    """
    Loads Excel files into pandas DataFrames.
    
    Parameters:
    - file_paths: List of strings, paths to the Excel files.
    
    Returns:
    - A dictionary with keys as (file_path, sheet_name) and values as DataFrames.
    """
    dfs = {}
    for file_path in file_paths:
        try:
            xls = pd.ExcelFile(file_path)
            for sheet_name in xls.sheet_names:
                df = pd.read_excel(xls, sheet_name=sheet_name)
                key = (file_path, sheet_name)
                dfs[key] = df
                # Print the first 10 rows of the loaded DataFrame
                print(f"First 10 rows of {file_path} - Sheet: {sheet_name}")
                print(df.head(10))  # head(10) displays the first 10 rows
            print(f"Loaded {file_path} successfully.")
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
    return dfs

def main():
    # Exclude the script name, get only file paths
    file_paths = sys.argv[1:]
    if not file_paths:
        print("No files provided. Usage: programname.py file1.xlsx file2.xlsx file3.xlsx")
        return
    
    # Load the Excel files into DataFrames
    data_frames = load_excel_files(file_paths)
    
    # For demonstration: print out the keys to show what was loaded
    print("\nLoaded DataFrames:")
    for key in data_frames.keys():
        print(f"{key[0]} - Sheet: {key[1]}")

if __name__ == "__main__":
    main()
