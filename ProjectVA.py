import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser 
import os
import pywhatkit
import random
import sys
import re
import requests
import urllib
import urllib3
import pyowm
import tkinter
import json
from tkinter import messagebox 
from PyDictionary import PyDictionary



    


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening")

    speak("I am TARS!")
    


def takeCommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio =r.listen(source)
    try:
        print("Recognizing....")

        query = r.recognize_google(audio, language='en-in')

        query.lower()
        print(f"User said: {query}\n")

        
        

    except Exception as e:
        print(e)

        speak("say that again please")

        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()
        if "wikipedia" in query.lower():
            speak("Searching Wikipedia")
            query=query.replace("wikipedia","")

            results = wikipedia.summary(query, sentences=1)

            speak("According to Wikipedia")
            speak(results)

        elif "open stackoverflow" in query.lower():
            webbrowser.open("stackoverflow.com")

        elif "open" in query.lower():
            domain = query.split(" ")
            print(domain[1])

            url = "https://www.{}.com".format(domain[1])
            webbrowser.open(url)
            print(url)
            sys.exit()
            speak('the website you have requested has been opened for you.')
            
        elif "the time" in query.lower():
            strTime = datetime.datetime.now().strftime("%H:%M:%S:") 
            speak(f"the time is {strTime}")

       
        elif "weather" in query.lower():
            
            print(query)

            url = format(query)
            webbrowser.open(url)
            print(url)
            sys.exit()
            speak('Weather is fetched on browser')

        elif "play" in query.lower():

            song = query.replace('play', '')
            speak("Playing" + song)  
            pywhatkit.playonyt(song)  

        elif "music" in  query.lower():
            music_dir = "C:\\Users\\Anil Dixit\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            num = random.randint(0, 1000)
            os.startfile(os.path.join(music_dir,songs[num]))
            print(songs[num])

        elif "stop" in query.lower():
            speak("Thanks!! Have a great day.")
            sys.exit()

        elif "meaning" in query.lower():
            dictionary=PyDictionary()
            mean = query.split(" ")
            word_meaning = dictionary.meaning(mean[0])
            print(word_meaning)
            speak(word_meaning)
    

            
            

    
           
