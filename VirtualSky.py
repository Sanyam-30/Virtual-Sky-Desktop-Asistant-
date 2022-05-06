import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import requests 
import subprocess

engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    
    else:        
        speak("Good Evening!")
    
    speak("I am Virtual Sky. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"  
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query= takeCommand().lower()

        if 'wikipedia' in query:
         speak('Searching Wikipedia...')
         query= query.replace("wikipedia","")
         results = wikipedia.summary(query,sentences=2)
         speak("According to Wikipedia")
         print(results)
         speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")           
    
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query: 
          music_dir='C:\\songs'
          songs = os.listdir(music_dir)
          speak("Playing music")
          print("Playing music")
          n = random.randint(1, 4)
          os.startfile(os.path.join(music_dir, songs[n]))
      
        elif 'the time' in query:
          strTime = datetime.datetime.now().strftime("%H:%M:%S")
          speak(f"Sir, the time is {strTime}")   
          
        elif 'open camera' in query:
           subprocess.run('start microsoft.windows.camera:', shell=True)
           
        elif 'joke' in query:
            speak(f"Hope you like this one sir")
            headers = {
             'Accept': 'application/json'
            }
            res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
            joke = res["joke"]
            speak(joke)
            print(joke)

        elif 'exit' in query:
            exit()   
  
      