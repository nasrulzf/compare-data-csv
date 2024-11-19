import pandas as pd
import csv

def search_items_in_csv(csv_file, search_column, search_list, output_file=None):
    """
    Search for a list of items in a specified column of a CSV file.
    
    Args:
        csv_file (str): Path to the input CSV file.
        search_column (str): Column name to search within.
        search_list (list): List of items to search for.
        output_file (str): Optional. Path to save the filtered rows as a CSV.
        
    Returns:
        DataFrame: Filtered rows containing the search items.
    """
    # Load the CSV file
    try:
        print(f"Start process file: {csv_file}")
        df = pd.read_csv(csv_file)
        print(f"Success load file: {csv_file}")
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return None
    
    # Check if the search column exists
    if search_column not in df.columns:
        print(f"Column '{search_column}' not found in the CSV file.")
        return None
    
    # Filter rows containing search items
    filtered_df = df[df[search_column].isin(search_list)]
    
    # Save to a new CSV file if specified
    if output_file:
        filtered_df.to_csv(output_file, index=False)
        print(f"Filtered data saved to '{output_file}'")
    
    return filtered_df

def csv_to_array(file_path, column_name):
    results = []    
    try:
        print(f"Read compare file: {file_path}")
        dfc = pd.read_csv(file_path)
        print(f"Success read compare file: {file_path}")
    except Exception as e:
        print(f"Error loading compare file: {e}")
        return None

    for i in range(len(dfc)):
        print(f"{dfc.values[i][0]}")
        results.append(f"{dfc.values[i][0]}")

    print(f"{len(results)} records for comparison found.")
    print(f"")

    return results

# Example usage
if __name__ == "__main__":
    # Specify input file, column, and search list
    csv_file = "2318237007.csv"  # Replace with your CSV file path
    search_column = "id_number"  # Replace with the column name to search
    compare_file = "compare.csv"
    search_list = csv_to_array(compare_file, "identityno")

    # Optionally save to a file
    output_file = "filtered_data.csv"  # Replace with your desired output file name

    # Search
    result = search_items_in_csv(csv_file, search_column, search_list, output_file)

    if result is not None:
        print("Search completed. Results:")
        print(result)