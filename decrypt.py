import PyPDF2 as pd
import os

pdf_name=str(input("Enter the full path of pdf file plus \\name_of_pdf_file.pdf -> "))

if os.path.exists(pdf_name) is False:
   print("Given PDF not found")
   exit()

pdf=open(r''+pdf_name,"rb")
pdfreader=pd.PdfFileReader(pdf)

if pdfreader.isEncrypted==False:
   print("Pdf is already decrypted")
   exit()

words=""
with open('dictionary.txt','r') as f:
     words=f.read()
words=words.split('\n')

l=len(words)
j=1
flag=False
for i in words:
    print(f"Matching Words --> {i}, {i.lower()}")
    print(f"{l-j} remaining..")
    pdfreader.decrypt(i)
    pdfreader.decrypt(i.lower())
    try:
         pdfreader.getPage(0)
         print(f"Access key -> {i}")
         flag=True
         break
    except:
          pass
    j+=1
if flag is False:
   print("Unable to crack!!")


#Program to encrypt pdf
#pdf_name=str(input("Enter the full path of pdf file plus \\name_of_pdf_file.pdf -> "))
#pass=str(input("Input password -> ")
#with open(r''+pdf_name,"rb") as in_file:
#    input_pdf=pd.PdfFileReader(in_file)
#    
#    output_pdf=pd.PdfFileWriter()
#    output_pdf.appendPagesFromReader(input_pdf)
#    output_pdf.encrypt(pass)
#    
#    with open("encrypted_file.pdf","wb") as out_file:
#         output_pdf.write(out_file)
#print(f"File saved with name encrypted_file.pdf")
