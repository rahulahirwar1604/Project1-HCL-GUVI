import pandas as pd
import os

class CSVAnalyzer:
    """
    A class to analyze CSV files:
    - Load CSV
    - Show structure, summary statistics, and missing values
    - Save report to text file
    - Clean data and save new CSV
    """

    def __init__(self, file_path):
        self.file_path = file_path    # Path to input CSV file
        self.df = None                # DataFrame to hold the CSV content
        self.report_lines = []        # List to store report strings

    def load_file(self):
        """Loads the CSV file into a pandas DataFrame."""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError("File not found.")

        try:
            self.df = pd.read_csv(self.file_path)
            print("File loaded successfully.\n")
        except Exception as e:
            raise Exception(f"Error reading CSV: {e}")

    def print_summary(self):
        """Generates and stores a summary report of the CSV content."""
        df = self.df

        self.report_lines.append("CSV File Analysis Report")
        self.report_lines.append("=" * 50)
        self.report_lines.append(f"File Path: {self.file_path}")
        self.report_lines.append(f"Shape (Rows, Columns): {df.shape}")
        self.report_lines.append(f"Column Names: {list(df.columns)}\n")

        # Data types of each column
        self.report_lines.append("Data Types:")
        self.report_lines.append(str(df.dtypes) + "\n")

        # First and last 5 rows
        self.report_lines.append("Top 5 Rows:")
        self.report_lines.append(str(df.head()) + "\n")

        self.report_lines.append("Bottom 5 Rows:")
        self.report_lines.append(str(df.tail()) + "\n")

        # Statistical summary
        self.report_lines.append("Summary Statistics:")
        self.report_lines.append(str(df.describe(include='all')) + "\n")

        # Unique values per column
        self.report_lines.append("Unique Values Per Column:")
        for col in df.columns:
            self.report_lines.append(f"{col}: {df[col].nunique()} unique values")
        self.report_lines.append("")

        # Missing values summary
        self.report_lines.append("Missing Values Per Column:")
        self.report_lines.append(str(df.isnull().sum()) + "\n")

        print("Analysis completed. Use `write_report()` to save to file.")

    def write_report(self, output_file="csv_analysis_report.txt"):
        """Writes the generated report to a text file."""
        with open(output_file, "w", encoding="utf-8") as file:
            file.write("\n".join(self.report_lines))
        print(f"Report saved as '{output_file}'.\n")

    def clean_data(self):
        """Drops rows with any missing values and returns the cleaned DataFrame."""
        if self.df is not None:
            cleaned_df = self.df.dropna()
            removed = len(self.df) - len(cleaned_df)
            print(f"Cleaned data: {removed} rows with missing values removed.\n")
            return cleaned_df
        else:
            raise Exception("No data loaded to clean.")

    def save_cleaned_csv(self, cleaned_df, output_file="cleaned_output.csv"):
        """Saves the cleaned DataFrame to a new CSV file."""
        cleaned_df.to_csv(output_file, index=False)
        print(f"Cleaned CSV saved as '{output_file}'.\n")


# ------------------- Driver Code -------------------

if __name__ == "__main__":
    # Ask user for input file
    file_path = input("Enter the path to your CSV file: ").strip()

    try:
        # Initialize the CSVAnalyzer object
        analyzer = CSVAnalyzer(file_path)

        # Load and analyze the file
        analyzer.load_file()
        analyzer.print_summary()
        analyzer.write_report()

        # Ask to clean and save data
        save_cleaned = input("Do you want to clean and save the CSV (drop missing rows)? (y/n): ").lower()

        if save_cleaned == 'y':
            cleaned = analyzer.clean_data()
            analyzer.save_cleaned_csv(cleaned)
        else:
            print("Cleaned CSV not saved.")

    except Exception as err:
        print(f"\nError: {err}")