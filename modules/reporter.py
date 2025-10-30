import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class Reporter:
    def generate_csv(self, data, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        print(f"CSV report saved: {filename}")

    def generate_pdf(self, data, filename):
        c = canvas.Canvas(filename, pagesize=letter)
        c.drawString(100, 750, "Crypto Tax Report")
        y = 700
        for row in data:
            c.drawString(100, y, str(row))
            y -= 20
        c.save()
        print(f"PDF report saved: {filename}")
