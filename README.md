# Excel dataframe Loader

This Python program loads Excel files into pandas DataFrames, making it easier to handle multiple sheets and files efficiently. It uses the pandas library for data manipulation and Excel file handling.

## Requirements

Before running this program, ensure you have Python installed on your system and the pandas library. You can install pandas using pip if you haven't already:

```
pip install pandas
```

## Usage

```
python load_df.py file1.xlsx file2.xlsx file3.xlsx
```

## Features

- **Multiple File Handling**: You can specify multiple Excel files as arguments.
- **Sheet-by-Sheet Loading**: Each sheet in the Excel files is loaded into a separate pandas DataFrame.
- **Error Handling**: The program gracefully handles and reports errors if a file cannot be loaded.
- **Preview Data**: For each sheet loaded, the program prints the first 10 rows to give you a quick peek at the data.

## Output

The program prints the first 10 rows of each sheet it loads to provide a quick overview of the data. It also prints a summary of the loaded files and sheets. The data is stored in a dictionary with keys as tuples of (file_path, sheet_name) and values as the respective DataFrames, which can be used for further processing in your Python code.
