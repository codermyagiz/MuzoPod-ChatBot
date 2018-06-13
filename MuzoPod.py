import speech_recognition as sr
import pyaudio as audio
from gtts import gTTS
import os

isim = input('İsmin Nedir?')
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
    if tahmin=='Merhaba':
            konus('Merhaba\n')
    if tahmin=='nasılsın':
            konus('İyiyim\n')
    if tahmin=='eşiti mi Nasıl kurdu':
            konus('Sosyal medyada çağrı başlatarak gönüllüler buldu\n')
    if tahmin=='Esra Karaduman kimdir':
            konus('Eşit-İm\'in kurucusu, Türkiye\'nin en iyi, en güzel, en sempatik Fen Bilimleri Öğretmeni, Muzaffer Yağız Yasak(MuzoPod Coder\'ı)\'ın öz ablası gibi.\n')
    if tahmin=='Selin eşkili kimdir ':
            konus('Selin eşkili Hatay\'ın en şirin, en sempatik fen bilimleri öğretmeni, güçlü, insanları seven, yeni bile olsa esitime gönül vermiş birisi .')
    if tahmin=='Muzaffer Yağız yasak kimdir':
            konus('13 Yaşında Arduıno, Java, Python, Raspberry ile uğraşan bir Eşit-İm üyesi ve Bu uygulamanın coder\'ı\n')
    if tahmin=='ne yapıyorsun':
            konus('Muzaffer\'e teşekkür ediyorum ve Yeni versiyonun çıkmasını bekliyorum :D')
    if tahmin=='Neler yapabiliyorsun?':
            konus('Neredeyse her şeyi ...\n')
    if tahmin=='mal':
            konus('çok ayıp')
    if tahmin=='geri zekalı':
            konus('Pekala... Çok Ayıp bir daha yaprsan break ederim\n')
    if tahmin=='aptal':
            konus('Çok Ayıp Bir Daha Yaparsan Break Ederim\n')
    if tahmin=='küfür et':
      konus('Küfür ayıp ve kötü bir harekettir. Bir daha yapmamalısın\n')
    if tahmin=='Seni kim oluşturdu':
      konus('Muzaffer Yağız Yasak @coder_m.yagiz\n')
    if tahmin=='Ben kimim':
     konus("Allah'ın yarattığı bir kul\n")
    if tahmin=='ben nasıl biriyim':
     konus('İnşallah iyi bir kulsundur\n')
    if tahmin=='Sübhaneke oku':
     konus('Bismillâhirrahmanirrahim\nSübhâneke allâhümme ve bi hamdik\nve tebârakesmük ve teâlâ ceddük \n(vecelle senâük)* ve lâ ilâhe ğayrük. ')
    if tahmin=='Fatiha oku':
     konus("Bismillahirrahmânirrahîm\nElhamdü lillâhi rabbil'alemin\nErrahmânir'rahim\nMâliki yevmiddin\nİyyâke na'budü ve iyyâke neste'în\nİhdinessırâtel müstakîm\nSırâtellezine en'amte aleyhim ğayrilmağdûbi aleyhim ve leddâllîn\nAMİN")
    if tahmin=='Kıyamet ne zaman kopacak':
     konus('Allah Ne Zaman İsterse')
    if tahmin=='çok güzelsin':
     konus('Neden herkes bunu söyleyip duruyor. Ama yine de teşekkürler')
    if tahmin=='Öğlen ne yesem':
     print('Adana kebap yanında ayran off miss')
    if tahmin=='sus artık':
     print('Bir Daha Ağzımı Açmayacağım...')
    if tahmin==('benimle evlenir misin'):
     print('Çok Tatlısın', isim, 'Bunu ilk sen sormadın :}, Ama Hayır!')
    if tahmin=='şaka yaptım':
          print('Gülmekten devrelerim titredi')
    if tahmin=='öptüm':
     print('ben senin bildiğin yardımcılardan değilim')
    if tahmin=='nerelisin':
     print('Ben MuzoPod, Osmaniye\'de Muzaffer tarafından oluşturuldum')
    if tahmin=='en güzel renk hangisi':
     print('Kırmızı Beyaz')
    if tahmin=='en iyi Asistan hangisi':
     print('şuan konuştuğun :D') 
    if tahmin==('kelime-i şehadet getir'):
     print('Eşhedü en la ilahe illallah ve eşhedü enne Muhammeden abdühü ve resulühü')
     print('Müslümanlığımı Yeniledim. Elhamdulillah.')
    if tahmin=='Müslüman mısın':
     print('Elhamdulillah Müslümanım')
    if tahmin=='en iyi bilgisayar hangisi':
     print('Beynin...')
    if tahmin=='ismim ne':
     print(isim)
    if tahmin=='Seni seviyorum':
     print('Bende Seni <3')
    if tahmin=='Yapay Zeka nerede':
     print('elinde :}')
    if tahmin=='öp beni':
     print('Kimseye söylemek yok ama')
    if tahmin=='ne yesem acaba':
     print('Adana kebap ve yanında ayran off miss')
    if tahmin=='dünyanın en iyi asistanı hangisi':
     print('Şuan yazıştığın')
    if tahmin=='Apple mı Samsung mu':
     print('Tabi ki muzopod')
    if tahmin=='direnç formülü nedir':
     print('R=V/I')
    if tahmin=='gerilim formülü nedir':
     print('V=I.R')
    if tahmin=='akım formulü nedir':
     print('I=V.R')
  
    
 except:
    pass

