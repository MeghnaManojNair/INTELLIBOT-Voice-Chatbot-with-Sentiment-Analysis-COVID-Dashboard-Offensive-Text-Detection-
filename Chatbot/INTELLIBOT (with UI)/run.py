from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import os
import time
import webbrowser
import datetime
import speech_recognition as sr



import pyttsx3
from time import ctime
import webbrowser
import time
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

flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good evening")

class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()

    def run(self):
        self.JARVIS()

    def STT(self):
        R = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listning...........")
            audio = R.listen(source)
        try:
            print("Recog......")
            text = R.recognize_google(audio,language='en-in')
            print(">> ",text)
        except Exception:
            speak("Sorry Speak Again")
            return "None"
        text = text.lower()
        return text

    def JARVIS(self):
        wish()
        while True:
            self.query = self.STT()
            if 'good bye' in self.query:
                sys.exit()
            if 'open google' in self.query:
                webbrowser.open('www.google.co.in')
                speak("opening google")
            if 'open youtube' in self.query:
                webbrowser.open("www.youtube.com")
            if 'play music' in self.query:
                speak("playing music from pc")
                self.music_dir ="./music"
                self.musics = os.listdir(self.music_dir)
                os.startfile(os.path.join(self.music_dir,self.musics[0]))
            if 'hello' in self.query:
                speak('Hey! Pleasure to meet you. What can I do for you?')
            if 'what is your name' in self.query:
                print('My name is INTELLIBOT')
                speak('my name is intellibot')
            if 'time' in self.query:
                print(ctime())
                speak(ctime())
            if 'search' in self.query:
                speak('what do  you want to search for')
                search = record_audio('What do you want to search for')
                url = 'https://google.com/search?q='+search
                webbrowser.get().open(url)
                print('Here is what I found for: '+ search)
                speak('here is what I found for: '+search)
            if 'find location' in self.query:
                speak('what is the location')
                location = record_audio('What is the location')
                url = 'https://google.nl/maps/place/'+location+'/&amp'
                webbrowser.get().open(url)
                print('Here is the location of: '+ location)
                speak('here is the location of: '+location)
            if 'food' in self.query:
                print('I dont need food for survival :)')
                speak('i dont need food for survival')
            if 'news' in self.query:
                url = 'https://timesofindia.indiatimes.com/home/headlines'
                webbrowser.get().open(url)
                speak('here are the top news headlines')
            if 'riddle' in self.query:
                print('What has to be broken before you can use it?')
                speak('What has to be broken before you can use it?')
                print('An egg')
                speak('an egg')
            if 'created' in self.query:
                print('I was made by Harika and Meghna')
                speak('I was made by Harika and Meghna')
            if 'offensive text detection' in self.query:
                url = 'https://theaiplayground.com/mnairmeghna/bot/Offensive-Text-Detection/view'
                webbrowser.get().open(url)
                speak('offensive text detection activating')
            if 'covid' in self.query:
                url = 'https://theaiplayground.com/mnairmeghna/bot/COVID-Dashboard/view'
                webbrowser.get().open(url)
                speak('covid dashboard activating')
            if 'emotion analysis' in self.query:
                url = 'https://theaiplayground.com/mnairmeghna/bot/Sentiment-Analysis/view'
                webbrowser.get().open(url)
                speak('sentiment analysis activating')
            if 'bye bye' in self.query:
                print('Bye!')
                speak('bye')
                exit()
FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

class Main(QMainWindow,FROM_MAIN):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1920,1080)
        self.label_7 = QLabel
        self.exitB.setStyleSheet("background-image:url(./lib/exit - Copy.png);\n"
        "border:none;")
        self.exitB.clicked.connect(self.close)
        self.setWindowFlags(flags)
        Dspeak = mainT()
        self.label_7 = QMovie("./lib/chatbot2.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)
        self.label_7.start()

        self.ts = time.strftime("%A, %d %B")

        Dspeak.start()
        self.label.setPixmap(QPixmap("./lib/tuse.png"))
        self.label_10.setText("<font size=8 color='white'>"+"INTELLIBOT"+"</font>")
        self.label_10.setFont(QFont(QFont('Acens',8)))
        self.label_5.setText("<font size=8 color='white'>"+self.ts+"</font>")
        self.label_5.setFont(QFont(QFont('Acens',8)))
        self.label_11.setText("<font size=7 color='white'>"+"Made by Meghna and Harika"+"</font>")
        self.label_11.setFont(QFont(QFont('Acens',8)))
        self.label_12.setText("<font size=8 color='white'>"+"Interact with me!!"+"</font>")
        self.label_12.setFont(QFont(QFont('Acens',8)))


app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())
