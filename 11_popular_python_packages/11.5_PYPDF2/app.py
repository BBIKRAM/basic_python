#install pypdf2
import PyPDF2

with open("History_Ancient_Medieval_Nepal.pdf","rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    total = reader.numPages
    print(total)
 
    page = reader.getPage(x)
    page.rotateClockwise(90)
    writer =PyPDF2.PdfFileWriter()
    # writer.addBlankPage()
    writer.addPage(page)
    with open("rotated.pdf","wb") as output:
            writer.write(output)