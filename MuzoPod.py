# -*- coding: utf-8 -*-
#encoding = utf8
import speech_recognition as sr
import pyaudio as audio
import os
import sys
import six
from io import open
from six.moves import input
from gtts import gTTS
import subprocess

if six.PY2:
    reload(sys)
    sys.setdefaultencoding('utf-8')

    from requests.packages import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print(u"İsmin Nedir?")
name = input()
qa = dict([x.split("\n") for x in open("tr.txt","r", encoding="utf-8-sig").read().split("\n\n")])

def speak(yazi, dil = "tr"):
    tts = gTTS(text=yazi, lang=dil) 
    tts.save("sound.mp3")   
    os.popen("ffplay -nodisp -loglevel panic -autoexit sound.mp3")

while True:
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print(u'Bir Şeyler Söyle')
        audio = r.listen(source)
        try:     
            question = r.recognize_google(audio, language="tr")
            print(u'MuzoPod Sizin Şunu Söylediğinizi Düşünüyor: ' + question)
            if estimate in qa.keys():
                answer = qa[question].replace("{name}",name)
                print(answer)
                speak(answer)
        except KeyboardInterrupt:
            break
        except:
            pass
