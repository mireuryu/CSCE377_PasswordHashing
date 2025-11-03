import pandas as pd

def delete_rows_below_line(input_file, output_file, line_number):
    """
    Keeps the header row and data up to the specified line number,
    deleting all rows below it.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file.
        line_number (int): The total number of lines (including header) to keep.
    """
    try:
        df = pd.read_csv(input_file)
        # Keep rows up to line_number - 1 (0-indexed)
        df_cleaned = df.iloc[:line_number - 1]
        df_cleaned.to_csv(output_file, index=False)
        print(f"Successfully kept the first {line_number} lines (including header) and saved to {output_file}")
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
delete_rows_below_line("data/pwlds_weak.csv", "data/pwlds_weak.csv", 100001)
