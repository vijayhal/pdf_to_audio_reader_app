
#  To speak python code  - pyttsx3
# import pyttsx3
#
# speaker = pyttsx3.init()
#
# speaker.say("hey, how r u")
#
# speaker.runAndWait()

# To read PDF  - PyPDF2

from pypdf import PdfReader
import pyttsx3

# book = open("OOP_BOOK.pdf", "rb")
#
# pdfReader = PyPDF2.PdfFileReader(book)

reader = PdfReader("OOP_BOOK.pdf")
number_of_pages = len(reader.pages)

print(number_of_pages)
speaker = pyttsx3.init()

for i in (1,number_of_pages):
    page = reader.pages[i]
    text = page.extract_text()

    speaker.say(text)

    speaker.runAndWait()