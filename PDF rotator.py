################################################################################
#                                   PDF ROTATOR                                #
################################################################################
# I scanned a document and it was upside down. Importing to word messed up the
# text. Adobe wants me to trial a product to be able to rotate it. Why not just
# expand my portfolio and make my own?


import os
import PyPDF2

current = os.getcwd()
print(current)

newdir = os.chdir('C:\\Users\\Jack\\Desktop')

pdf_in = open('.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_in)
pdf_writer = PyPDF2.PdfFileWriter()


for pagenum in range (pdf_reader.numPages):
      page = pdf_reader.getPage(pagenum)
      page.rotateClockwise(180)
      pdf_writer.addPage(page)

pdf_out = open('.pdf', 'wb')
pdf_writer.write(pdf_out)
pdf_out.close()
pdf_out.close()
