from reportlab.pdfgen import canvas


pdf = canvas.Canvas("data/sample_resume.pdf")

text = [
    "Kevin Njogu",
    "",
    "Python Developer",
    "",
    "Skills:",
    "Python",
    "Machine Learning",
    "SQL",
    "Git",
    "",
    "Experience:",
    "Built AI applications using Python and data analysis tools."
]

y = 750

for line in text:
    pdf.drawString(50, y, line)
    y -= 20

pdf.save()

print("Sample PDF created")