from googletrans import Translator
from gtts import gTTS
import os

text = input("Text >")

translator = Translator()
dtl = translator.detect(text)
transl = translator.translate(text, src=dtl.lang, dest='si')
ttext = transl.text
print(ttext)

myobj = gTTS(text=ttext, lang='si', slow=False)
myobj.save('D:\\s.mp3')

