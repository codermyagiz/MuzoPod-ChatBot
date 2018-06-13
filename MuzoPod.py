#encoding = utf8

import speech_recognition as sr
import pyaudio as audio
from gtts import gTTS
import os

isim = input('İsmin Nedir?')
qa = dict([x.split("\n") for x in open("tr.txt","r", encoding="utf8").read().split("\n\n")])

def konus(yazi, dil = "tr"):
    tts = gTTS(text=yazi, lang=dil) 
    tts.save("sound.mp3")
    os.system("ffplay -nodisp -loglevel panic -autoexit sound.mp3")

while True:
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Bir Şeyler Söyle')
        audio = r.listen(source)
        try:     
            tahmin = r.recognize_google(audio, language="tr")
            print('Google Sizin Şunu Söylediğinizi :\n' + tahmin)
            if tahmin in qa.keys():
                cevap = qa[tahmin].replace("{name}",isim)
                print(cevap)
                konus(cevap)
        except:pass