import pyttsx3
import PyPDF2
book = open('htwfaip.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
for num in range(24,pages):
    page = pdfReader.getPage(24)
    text =  page.extractText()
    speaker.say(text)
    speaker.runAndWait()
