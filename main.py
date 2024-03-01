import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[2].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!,sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!,sir")

    else:
        speak("Good Evening!,sir")


    speak("I am vision. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open chrome' in query:
            webbrowser.open("chrome.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif'open whatsapp' in query:
            webbrowser.open("whatsapp web")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open calculator' in query:
            webbrowser.open("calculator.net")

        elif 'open w3school' in query:
            webbrowser.open("w3schools.com")

        elif 'open spotify' in query:
            webbrowser.open("spotify.com")

        elif 'stop' in query:
            sys.exit()
        elif 'playlist' in query:
            webbrowser.open('https://youtu.be/NmS9qjvUCKQ?si=rBjcc8_tGVqwRAAh')
        elif 'instagram' in query:
            webbrowser.open('instagram.com')
