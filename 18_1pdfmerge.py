from PyPDF2 import PdfFileMerger

pdfs = ['static\\1.pdf', 'static\\2.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("3.pdf")
merger.close()