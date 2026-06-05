import speech_recognition as sr
import webbrowser
import pyttsx3
# import gtts as gTTS
import musiclibrary
import requests
from openai import OpenAI
from client import ai_process

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi_key = "d7d40341ebf140e2bd42921a4ee6d43c" 

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def processcommand(command):
    if 'goodbye jarvis' in command:
        speak("Goodbye! Have a great day!")
        exit()
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "play" in command:
        song_name = command.split(' ')[1]
        print(song_name)
        speak(f"Playing {song_name} for you")
        link = musiclibrary.songs.get(song_name)
        webbrowser.open(link)
    elif "news" in command:
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi_key}"
        response = requests.get(url)
        if( response.status_code == 200):
            data = response.json()
            articles = data.get("articles",[])
            for i, article in enumerate(articles):
                if i >= 5:
                    break
                speak(f"Article {i+1}: {article['title']}")
    else:
        #Let open AI handle the request
        output = ai_process(command)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while(True):
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Jarvis is ready to assist you.")
                print("Say Jarvis to start.....")
                audio = r.listen(source,timeout=4, phrase_time_limit=2)
            words = r.recognize_google(audio)

            if 'bye jarvis' in words.lower():
                speak("Goodbye! Have a great day!")
                break
            
            if 'jarvis' in words.lower():
                speak("Yaa how can I help you?")
                with sr.Microphone() as source:
                    print("Jarvis is ready to assist you.")
                    print("Listening.....")
                    audio = r.listen(source,timeout=12, phrase_time_limit=4)
                    print("Recognizing.....")
                    words = r.recognize_google(audio)
                    print(f"You said: {words}")
                processcommand(words.lower())


        except Exception as e:
            print(e)