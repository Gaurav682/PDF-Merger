import PyPDF2

pdfFiles = ["1.pdf", "2.pdf"]
merger = PyPDF2.PdfMerger()
for filename in pdfFiles:
    pFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pFile)
    merger.append(pdfReader)

pFile.close()
merger.write('merged.pdf')
