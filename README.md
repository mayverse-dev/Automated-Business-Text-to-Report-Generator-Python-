# 📊 Automated Business Report Generator (Python)

![Project Demo](view before and after.png)
*(Above: Raw unstructured log files automatically converted into a clean PDF report in 0.5 seconds)*

## 🛑 The Business Problem
Many businesses generate massive amounts of "unstructured data"—server logs, daily delivery notes, or survey responses—that are stored as messy text files. 
Managers often waste **5-10 hours per week** manually copying this data into Excel or Word to create reports, leading to human error and lost time.

## ✅ The Solution
I built a custom Python automation engine that ingests raw text files, intelligently identifies key data points (using Regex patterns), and auto-generates a **Management-Ready PDF Report**.

Unlike generic tools, this script:
1.  **Parses Messy Text:** extracting only relevant data (ID, Status, Error Codes).
2.  **Visualizes Critical Issues:** Automatically highlights "Errors" or "Delays" in RED for immediate attention.
3.  **Formats Professionally:** Generates a branded PDF with headers, footers, and timestamps.

## 🛠 Key Features
* **Custom Data Parsing:** Can be adapted to read *any* log format (CSV, .txt, .log).
* **Conditional Formatting:** The script detects specific keywords (e.g., "ERROR", "URGENT") and styles them differently.
* **Zero Dependencies:** Runs locally on any machine with Python installed.

## 💼 Potential Use Cases
While this demo processes **Logistics/Trucking Data**, the core engine is designed to handle:
* **IT Server Logs:** Extracting "Critical Failures" from millions of lines of code.
* **Medical Records:** Summarizing patient check-in notes into a daily digest.
* **Customer Surveys:** Compiling free-text feedback into a readable list.

THANK YOU FOR YOUR TIME

