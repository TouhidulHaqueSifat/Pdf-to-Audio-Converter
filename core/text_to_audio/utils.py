from pypdf import PdfReader
import pyttsx3

class ExtarctText:

    def extract_text_from_pdf(self, pdf_path,start_page,end_page):
        reader = PdfReader(pdf_path)
        text = ""
        number_of_page = len(reader.pages)
        if start_page < 0 or end_page >=number_of_page or start_page > end_page:
            raise ValueError("Invalid page range")
        
        for i in range(start_page, end_page+1):
            number_of_page = len(reader.pages)

            if i < number_of_page:
                text += reader.pages[i].extract_text() or ""
        return text
            
class ConvertToAudio:
    
    def __init__(self):
        self.engine = pyttsx3.init()

    def convert_to_audio(self,text,filename= None):
       self.engine.setProperty('rate',150)
       self.engine.setProperty('volume',1.0)
       voices = self.engine.getProperty('voice')
       #self.engine.save_to_file(text,filename)
       print(voices)
       self.engine.say(text)
       self.engine.runAndWait()

t1 = ConvertToAudio()
t1.convert_to_audio(''' purpose of this book is to give you a thorough introduction to competitive
                            programming.''')