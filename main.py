import pyttsx3
import speech_recognition as sr
from datetime import datetime
import wikipedia
import webbrowser
import os
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(text)
    engine.runAndWait()
def welcome():
    '''welcome() function wishes the user and introduces friday to the user'''
    hrs = int(datetime.now().hour)
    if(hrs<12):
        speak("Good morning")
        print("Good morning")
    else:
        speak('Good afternoon')
        print("Good afternoon")
    speak("I am friday! How can I help you")
    print("I am friday! how can I help you")

def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listining.......")
        audio_txt = r.listen(source)
        r.pause_threshold = 1
    try:
        query = r.recognize_google(audio_txt,language='en-in')
    except Exception as e:
        print('Please say again!')
    return query

if __name__ == "__main__":
        welcome()
        while True:
            query = Listen().lower()
            if "open youtube" in query:
                print("opening youtube")
                speak("opening youtube")
                webbrowser.open("youtube.com")
            elif "open google" in query:
                print("opening google")
                speak("opening google")
                webbrowser.open('google.com')
            elif "open codechef" in query:
                print("opening codechef")
                speak("opening codechef")
                webbrowser.open('codechef.com')
            elif "search wikipedia" in query:
                print("searching wikipedia..........")
                speak("searching wikipedia")
                query.replace("search wikipedia for","")
                print("Wikipedia says,"+ wikipedia.summary(query,sentences=2))
                speak("Wikipedia says,"+ wikipedia.summary(query,sentences=2))
            elif "play movie" in query:
                query.replace("play movie","")
                list  = [entry.name for entry in os.scandir("E:\\my movies\\english movies\\")]
                print("Opening............")
                speak("opening............")
                os.startfile("E:\\my movies\\english movies")