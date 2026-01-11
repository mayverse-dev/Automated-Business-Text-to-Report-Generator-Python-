from fpdf import FPDF
import re


class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Daily Logistics Report', 1, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, 'C')


def generate_report(input_file, output_pdf):
    print("Reading file...")

    errors = []
    delays = []

    with open(input_file, 'r') as file:
        for line in file:
            if "ERROR" in line:
                truck_id = re.search(r'TRUCK_ID:(\d+)', line).group(1)
                reason = re.search(r'REASON:(\w+)', line).group(1)
                errors.append((truck_id, reason))
            elif "DELAYED" in line:
                delays.append(line.strip())

    print("Generating PDF...")
    pdf = PDFReport()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "1. Executive Summary", 0, 1)

    pdf.set_font("Arial", size=11)
    pdf.cell(0, 10, f"- Critical Errors Found: {len(errors)}", 0, 1)
    pdf.cell(0, 10, f"- Delays Reported: {len(delays)}", 0, 1)
    pdf.ln(5)

    pdf.set_font("Arial", 'B', 12)
    pdf.set_text_color(255, 0, 0)
    pdf.cell(0, 10, "2. Critical Errors (Action Required)", 0, 1)

    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", size=10)

    # Draw Table Header
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(40, 10, "Truck ID", 1, 0, 'C', 1)
    pdf.cell(100, 10, "Issue Detected", 1, 1, 'C', 1)

    for error in errors:
        truck_id = error[0]
        issue = error[1]
        pdf.cell(40, 10, truck_id, 1, 0, 'C')
        pdf.cell(100, 10, issue, 1, 1, 'C')

    pdf.output(output_pdf)
    print(f"✅ Success! Report saved as: {output_pdf}")


generate_report('delivery_log.txt', 'Daily_Report.pdf')
