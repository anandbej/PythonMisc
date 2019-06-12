# importing required modules
# import PyPDF2 
import pyttsx3;
import subprocess
import pdftotext


def textToWav(text,file_name):
   subprocess.call(["espeak", "-w"+file_name+".wav", "-g 15", "-v+m1", text])


# creating a pdf file object 
pdfFileObj = open('itoohadluvstory.pdf', 'rb') 
# pdfFileObj = open('sample.pdf', 'rb') 

# Load your PDF
with pdfFileObj as f:
    pdf = pdftotext.PDF(f)

# If it's password-protected
# with open("secure.pdf", "rb") as f:
#     pdf = pdftotext.PDF(f, "secret")

# How many pages?
# print(len(pdf))

# Iterate over all the pages
final = "\n\n".join(pdf);
print final
# exit();

pdfFileObj.close() 
textToWav(final,'itoohadluvstory')
