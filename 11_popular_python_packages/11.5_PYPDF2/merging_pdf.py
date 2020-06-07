import PyPDF2

merger = PyPDF2.PdfFileMerger()
pdf_list= ["History_Ancient_Medieval_Nepal.pdf","History_Ancient_Medieval_Nepal.pdf"]
for pdf_lists in pdf_list:
    merger.append(pdf_lists)
merger.write("comdine.pdf")