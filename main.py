import pyttsx3
import PyPDF2
import speech_recognition as sr
import datetime

#engine setup 

engine =pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices',voices[0].id)

#creating speak function

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#speech command 
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout = 2,phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'user said: {query}')

    except Exception as e:
        speak("Say that again please....")
        return "none"
    return query

#wish function 
def wish():
    hour = int(datetime.datetime.now().hour)
    minute = datetime.datetime.now().strftime("%H:%M:%S")
    speak("Hello boss!")
    if hour>=0 and hour<=12:
        speak("Good morning Sir")
        speak(f'right now time is {minute}')
    elif hour>=12 and hour<=18:
        speak("Good afternoon")
        speak(f'right now time is {minute}')
    else:
        speak("Good evening")
        speak(f'right now time is {minute}')
    speak("I am legion , Online and ready to help")

#main program 
wish()
speak("Welcome to Pdf reader")
speak("Which mode do you want to select")
quary = takecommand().lower()
while True:
   if "specific page" in quary:
        speak("please speak up the page which you want to read")
        quary2 = takecommand().lower()
        book = open('CHECKLIST.pdf', 'rb')
        pdfReader = PyPDF2.PdfFileReader(book)
        page = pdfReader.getPage(int(quary2) - 1)
        text = page.extractText()
        speak(text)
   elif "book" in quary:
        book = open('CHECKLIST.pdf', 'rb')
        pdfReader = PyPDF2.PdfFileReader(book)
        number = pdfReader.numPages
        for list in range(0,number):
            page = pdfReader.getPage(list)
            text = page.extractText()
            speak(text)
        
            
