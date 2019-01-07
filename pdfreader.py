# importing required modules 
# from gtts import gTTS
import PyPDF2 
import pyttsx3;
import subprocess

def textToWav(text,file_name):
   subprocess.call(["espeak", "-w"+file_name+".wav", "-g 15", "-v+m1", text])


# creating a pdf file object 
pdfFileObj = open('itoohadluvstory.pdf', 'rb') 

# print pdfFileObj
# exit();

# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
# engine = pyttsx3.init();
# rate = engine.getProperty('rate')
# engine.setProperty('rate', rate-100)
# engine.setProperty('voice', 'tamil')
# engine.say("I will speak this text");
# engine.runAndWait() ;
# voices = engine.getProperty('voices')
# for voice in voices:
# 	print voice.id
#    # engine.say('The quick brown fox jumped over the lazy dog.')
# # engine.runAndWait()
# exit();

# printing number of pages in pdf file 
# print(pdfReader.numPages) 
Npages = pdfReader.numPages
final = ''
for x in xrange(0,Npages):
	if x > 10:
		print x
		print pdfReader.getPage(x).extractText()
		# pass
	# final += pdfReader.getPage(x).extractText() 
	# engine.say(pdfReader.getPage(x).extractText());
	# engine.runAndWait() ;
	print final
	# exit();

textToWav(final,'itoohadluvstory')

# creating a page object 
pageObj = pdfReader.getPage(0) 




# tts = gTTS(text='what to say', lang='en')
# tts.save('/path/to/file.mp3')

# print "\n\n\n"
# # extracting text from page 
# print(pageObj.extractText()) 

# closing the pdf file object 
pdfFileObj.close() 
