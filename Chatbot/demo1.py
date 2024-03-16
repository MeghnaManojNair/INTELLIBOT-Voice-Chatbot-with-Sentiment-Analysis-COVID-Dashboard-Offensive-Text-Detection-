#-------------Working code for STT and TTS----------------#
import speech_recognition as sr
import pyttsx3
from time import ctime
import webbrowser
import time

#chatbot
r = sr.Recognizer()
def record_audio(ask=False):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        if ask:
            print(ask)
        audio = recognizer.listen(source)
        voice_data = ''
        try:
            voice_data = recognizer.recognize_google(audio)
        except sr.UnkownValueError:
            print('Sorry, I didn\'t get you')
        except sr.RequestError:
            print('Sorry, my speech service is down')
        return voice_data

def speak(audio):
    text_speech = pyttsx3.init()
    answer = audio
    text_speech.say(answer)
    text_speech.runAndWait()

def respond(voice_data):
    if 'hello' in voice_data:
        print('Hey! Pleasure to meet you. What can I do for you?')
        speak('Hey! Pleasure to meet you. What can I do for you?')
    if 'what is your name' in voice_data:
        print('My name is INTELLIBOT')
        speak('my name is intellibot')
    if 'time' in voice_data:
        print(ctime())
        speak(ctime())
    if 'search' in voice_data:
        speak('what do  you want to search for')
        search = record_audio('What do you want to search for')
        url = 'https://google.com/search?q='+search
        webbrowser.get().open(url)
        print('Here is what I found for: '+ search)
        speak('here is what I found for: '+search)
    if 'find location' in voice_data:
        speak('what is the location')
        location = record_audio('What is the location')
        url = 'https://google.nl/maps/place/'+location+'/&amp'
        webbrowser.get().open(url)
        print('Here is the location of: '+ location)
        speak('here is the location of: '+location)
    if 'food' in voice_data:
        print('I dont need food for survival :)')
        speak('i dont need food for survival')
    if 'news' in voice_data:
        url = 'https://timesofindia.indiatimes.com/home/headlines'
        webbrowser.get().open(url)
        speak('here are the top news headlines')
    if 'riddle' in voice_data:
        print('What has to be broken before you can use it?')
        speak('What has to be broken before you can use it?')
        print('An egg')
        speak('an egg')
    if 'created' in voice_data:
        print('I was made by Harika and Meghna')
        speak('I was made by Harika and Meghna')
    if 'offensive text detection' in voice_data:
        url = 'https://theaiplayground.com/mnairmeghna/bot/Offensive-Text-Detection/view'
        webbrowser.get().open(url)
        speak('offensive text detection activating')
    if 'covid' in voice_data:
        url = 'https://theaiplayground.com/mnairmeghna/bot/COVID-Dashboard/view'
        webbrowser.get().open(url)
        speak('covid dashboard activating')
    if 'sentiment analysis' in voice_data:
        url = 'https://theaiplayground.com/mnairmeghna/bot/Sentiment-Analysis/view'
        webbrowser.get().open(url)
        speak('sentiment analysis activating')
    if 'bye bye' in voice_data:
        print('Bye!')
        speak('bye')
        exit()

time.sleep(1)
print('Hello there! How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
