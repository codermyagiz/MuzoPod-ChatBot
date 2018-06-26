from tkinter import *
import speech_recognition as sr
qa = dict([x.split("\n") for x in open("tr.txt","r", encoding="utf-8-sig").read().split("\n\n")])

def speak(yazi, dil = "tr"):
    tts = gTTS(text=yazi, lang=dil) 
    tts.save("sound.mp3")   
    os.popen("ffplay -nodisp -loglevel panic -autoexit sound.mp3")


def dur():
    print("Sustum")
def kbb():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print(u'Bir Şeyler Söyle')

        audio = r.listen(source)
        try:     
            estimate = r.recognize_google(audio, language="tr")
            print(u'MuzoPod Sizin Şunu Söylediğinizi Düşünüyor: ' + estimate)
            if estimate in qa.keys():
                answer = qa[estimate].replace("{name}",name)
                print(answer)
                speak(answer)
        except:
            pass

root = Tk()
frame = Frame(root)
root.title('MuzoPod')
yukari_yazisi = Label(frame, text="MuzoPod'a Hoş Geldiniz", bg="yellow", fg="black")
yukari_yazisi.pack(fill=X,pady=0)

root.geometry("360x180")
frame.pack()

button = Button(frame, text="Konuşma\nButonu", command=kbb)
button.config( height = 10, width = 10 )
button.pack(side=RIGHT)
slogan = Button(frame,text="Susma\nButonu",command=dur)
slogan.config( height = 10, width = 10 )
slogan.pack(side=LEFT)
root.mainloop()
