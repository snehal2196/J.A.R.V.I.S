import os

import datetime as datetime
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    pass

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<=12:
        speak('Good Morning!')
    elif hour>12 and hour<18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')
    speak('I am Jarvis! Please tell me how may i help you.')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        #r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='hn-IN')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again..")
        return 'None'
    return query

if __name__ == '__main__':
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            print(results)

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTme = datetime.datetime.now().strftime('%H:%M;%S')
            speak(f'The time is {strTme}')

        elif 'open code' in query:
            codepath = "C:\\Users\\Snehal\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codepath)

        elif 'open code' in query:
            codepath = "C:\\Users\\Snehal\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.close(codepath)



