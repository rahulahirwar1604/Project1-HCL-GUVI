import streamlit as st
import pandas as pd
from csv_analyzer_oop_clean import CSVAnalyzer


st.set_page_config(page_title="CSV File Analyzer", layout="wide")

st.title("📊 CSV File Analyzer")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Save the uploaded file to a temporary location
    with open("temp_uploaded.csv", "wb") as f:
        f.write(uploaded_file.getbuffer())

    try:
        # Initialize analyzer
        analyzer = CSVAnalyzer("temp_uploaded.csv")
        analyzer.load_file()

        # Display preview and stats
        st.subheader("Dataset Preview")
        st.dataframe(analyzer.df.head())

        # Generate report
        analyzer.print_summary()

        st.subheader("Analysis Summary")
        for line in analyzer.report_lines:
            st.text(line)

        # Allow downloading the report
        if st.button("Download Report as .txt"):
            with open("csv_analysis_report.txt", "w", encoding="utf-8") as f:
                f.write("\n".join(analyzer.report_lines))

            with open("csv_analysis_report.txt", "r", encoding="utf-8") as file:
                st.download_button("Download Now", file.read(), file_name="csv_analysis_report.txt")

        # Option to clean data
        st.subheader("Clean Data")
        if st.button("Drop Rows with Missing Values"):
            cleaned_df = analyzer.clean_data()
            st.dataframe(cleaned_df.head())

            csv = cleaned_df.to_csv(index=False).encode("utf-8")
            st.download_button("Download Cleaned CSV", csv, file_name="cleaned_output.csv")

    except Exception as e:
        st.error(f"An error occurred: {e}")