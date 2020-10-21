import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("Good Morning!")
    elif hour >=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am leea, Please tell me how can i help you ?")

def TakeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...............")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..............")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception:
        print("Say that again please ........")
        return "None"
    return query

if __name__ == "__main__":
    
    WishMe()
    while True:
        query = TakeCommand().lower()

        if "wikipedia" in query:
            speak("Searching Wikipedia......")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
            speak("opening youtube")
        
        elif "open google" in query:
            webbrowser.open("google.com")
            speak("opening google")

        elif "open instagram" in query:
            webbrowser.open("instagram.com")
            speak("opening instagram")

        elif "play music" in query:
            music_dir = 'A:\\songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[2]))
            speak("playing music")

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(strTime)
            print(strTime)

        elif "quit" in query:
            speak("Thank you for using me")
            quit()
