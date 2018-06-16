#encoding = utf8

import speech_recognition as sr
import pyaudio as audio
from gtts import gTTS
import os

name = input('İsmin Nedir?')
qa = dict([x.split("\n") for x in open("tr.txt","r", encoding="utf8").read().split("\n\n")])

def speak(yazi, dil = "tr"):
    tts = gTTS(text=yazi, lang=dil) 
    tts.save("sound.mp3")
    os.system("ffplay -nodisp -loglevel panic -autoexit sound.mp3")

while True:
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Bir Şeyler Söyle')
        audio = r.listen(source)
        try:     
            estimate = r.recognize_google(audio, language="tr")
            print('MuzoPod Sizin Şunu Söylediğinizi Düşünüyor :\n' + estimate)
            if estimate in qa.keys():
                answer = qa[estimate].replace("{name}",name)
                print(answer)
                speak(answer)
        except:pass
