import py PDF2
import sys
import os
merger = pyPDF2.pdffilemerger()
for file in os.listdir(os.curdir):
       if file.endswith(".pdf"):
               print(file)

               merger.append(file)
               merger.write("BusinessPlanSolarCompanypdf")
