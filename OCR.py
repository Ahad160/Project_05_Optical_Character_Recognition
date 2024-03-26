from pytesseract import pytesseract
import os

class OCR:
    def __init__(self):
        self.path = r'E:\Software\Tesseract-OCR\tesseract.exe'

    def Extract(self,Filename):

       try: 
            pytesseract.tesseract_cmd = self.path
            text= pytesseract.image_to_data(Filename)

            file=open("data.txt",'w')
            file.write(text)
            file.close()

       except Exception as error:
         print(error)


object=OCR()

print(object.Extract('DG.jpg'))