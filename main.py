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
from config import apikey
import random

male = 1

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[male].id)

chatstr = ""


def changeVoice():
    global male
    if male == 1:
        male= 0
    else:
        male = 1
    engine.setProperty('voice', voices[male].id)


def ai(text):
    openai.api_key = apikey
    prompt = f"OpenAi response for {text}"
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=text,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        query = response["choices"][0]["text"]
        prompt += query
        if not os.path.exists("Openai"):
            os.mkdir("Openai")
            
        with open(f"Openai/{' '.join(text.split('intelligence')[1:]).strip()}","w") as f:
            f.write(prompt)
            
    except:
        query = "cannot process data"
    
    return query

def chat(query):
    global chatstr
    openai.api_key = apikey
    chatstr += f"Pritam: {query}\n Garuda(An AI created by Pritam): "
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=chatstr,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        res = response['choices'][0]['text']
        chatstr += f"{res}\n"
        return res
        
        # if not os.path.exists("Openai"):
        #     os.mkdir("Openai")
            
        # with open(f"Openai/{' '.join(text.split('intelligence')[1:]).strip()}","w") as f:
        #     f.write(prompt)
            
    except:
        res = "cannot process data"
    
    return res
    

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
                
        if "none" in text:
            continue
        
        elif "open chrome" in text:
            say("Opening File")
            path = "https://codeforces.com/"
            path = os.path.realpath(path)
            webbrowser.open(path)
            
        elif "the time" in text:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir the time is {hour} hour {min} minutes")
            
        elif "change your voice" in text:
            say("Changing my voice")
            changeVoice()
            say("My voice is changed")
        
        elif "now stop" in text:
            say("Garuda exiting Thank you")
            break
        
        elif "using artificial intelligence" in text:
            prompt = ai(text)
            print(prompt)
            # say(prompt)
            
        else:
            query = chat(text)
            say(query)
            # print(chatstr)
            