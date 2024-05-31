from pypdf import PdfWriter

merger = PdfWriter()

for pdf in ["pdf_one.pdf", "pdf_two.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
