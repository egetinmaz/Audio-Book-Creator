import pyttsx3
import PyPDF2
from tkinter.filedialog import *

# Initialize the PDF reader and define book variable
book = askopenfilename()
pdfreader = PyPDF2.PdfReader(book)
pages = len(pdfreader.pages)

# Gather the text from each page of the PDF
for num in range(0, pages):
    page = pdfreader.pages[num]
    text = page.extract_text()
    
    # Initialize the text-to-speech engine
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()
