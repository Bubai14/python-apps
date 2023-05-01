from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
# Prevent pdf from page break automatically
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv('topics.csv')


def add_footer(ln, topic):
    pdf.ln(ln)
    pdf.set_font(family="Times", style="I", size=10)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=topic, align="R")


for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(255, 153, 0)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)
    pdf.line(10, 19, 200, 19)

    # Adding a footer
    add_footer(265, row["Topic"])

    for i in range(row['Pages'] - 1):
        pdf.add_page()
        # Adding a footer
        add_footer(277, row["Topic"])

pdf.output(name="output.pdf")
