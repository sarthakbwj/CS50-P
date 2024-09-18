from fpdf import FPDF

name = input("Name: ")
pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 45)
pdf.cell(0,60, "CS50 Shirtificate", align="C")
pdf.image("shirtificate.png", x=0, y=70)
pdf.set_font_size(40)
pdf.set_text_color(255, 255, 255)
pdf.text(x = 43, y = 145, text=f"{name} took CS50")
pdf.output("Shirtficate.pdf") 