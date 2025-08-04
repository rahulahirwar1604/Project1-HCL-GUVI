
# 📊 Basic CSV File Analyzer

A beginner-friendly tool built with **Python** and **Streamlit** to analyze and clean CSV files. It helps users explore datasets by showing file structure, column types, summary statistics, missing values, and allows exporting cleaned versions.

---

## 📁 Project Structure

```
Project1-HCL-GUVI/
├── csv_analyzer_oop_clean.py     # OOP logic for loading, analyzing, and cleaning CSV
├── app.py                        # Streamlit web app interface
├── csv_analysis_report.txt       # Generated analysis report (after running)
└── cleaned_output.csv            # Cleaned dataset (optional, if saved)
```

---

## ⚙️ Requirements

Make sure you have Python 3.7 or above. Then install dependencies:

```bash
pip install pandas streamlit
```

---

## 🚀 How to Run the Project

### 1. Run via CLI (Console Version)

If you want to run it through the command line:

```bash
python csv_analyzer_oop_clean.py
```

You’ll be asked to input the CSV file path, and the program will generate:
- Terminal output with summary
- A `csv_analysis_report.txt` file
- An optional `cleaned_output.csv` if you choose to save cleaned data

---

### 2. Run via Streamlit (Web Version)

Start the web app with:

```bash
streamlit run app.py
```

Then:
- Upload a CSV file via the web UI
- View the dataset preview and summary
- Download a `.txt` report
- Clean and export the dataset if needed

---

## 📦 Features

- Load and preview any CSV file
- View data shape, column names, and data types
- Summary statistics (`describe()`)
- Count missing and unique values
- Save analysis report as `.txt`
- Clean data by removing rows with nulls
- Save cleaned data as a new CSV
- Web UI with Streamlit for interactive use

---

## 🧠 Concepts Used

- Python OOP (Object-Oriented Programming)
- Pandas for data manipulation
- File I/O for saving reports and data
- Streamlit for web UI

---

## 🔧 Future Improvements

- Upload Excel files (.xlsx)
- Display data quality score
