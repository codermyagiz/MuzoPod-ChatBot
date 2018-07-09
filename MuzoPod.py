# -*- coding: utf-8 -*-
#encoding = utf8
#!/usr/bin/env python 
import speech_recognition as sr
import pyaudio as audio
import os
import sys
import six
import tkinter as tk
import subprocess
import json
import codecs

from io import open
from six.moves import input
from six.moves.urllib.request import urlopen
from six.moves.urllib.parse import quote_plus    
from gtts import gTTS

if six.PY2:
    reload(sys)
    sys.setdefaultencoding('utf-8')

    from requests.packages import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

r = sr.Recognizer()
reader = codecs.getreader("utf-8")

print(u"İsmin Nedir?")
name = input()

def speak(yazi, dil = "tr"):
    tts = gTTS(text=yazi, lang=dil) 
    tts.save("sound.mp3")   
    os.popen("ffplay -nodisp -loglevel panic -autoexit sound.mp3")

while True:
    with sr.Microphone() as source:
        print(u'Bir Şeyler Söyle')

        audio = r.listen(source)
        try:     
            prediction = r.recognize_google(audio, language="tr")
            print(u'MuzoPod Sizin Şunu Söylediğinizi Düşünüyor: ' + prediction)

            response = json.load(reader(urlopen("http://muzopod.herokuapp.com/ask?sentence={}".format(quote_plus(prediction.lower().encode('utf8'))))))
            if response["status"]:
                answer = response["answer"].replace("{name}",name)
                print(answer)
                speak(answer)
        except KeyboardInterrupt:
            break
        except sr.UnknownValueError:
            pass