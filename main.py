import speech_recognition as sr
# import os
import pyaudio 
import wikipedia
import openai
import pyttsx3
import webbrowser
import datetime
import subprocess,os
from sitesfile import sites

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def say(text):
    engine.say(text)
    engine.runAndWait()
    

def takeCommand() :
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query
    
if __name__ == '__main__':
    say("Hello I am Garuda")
    while True :
        print("Listening...")
        text = takeCommand()
        text = text.lower();
        # say(text)
        
        for site in sites :
            if f"open {site[0]}" in text.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        
        if "open chrome" in text:
            say("Opening File")
            path = "https://codeforces.com/"
            path = os.path.realpath(path)
            webbrowser.open(path)
            
        if "the time" in text:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir the time is {hour} hour {min} minutes")
            
        
        
        if "now stop" in text:
            say("Garuda exiting Thank you")
            break