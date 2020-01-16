# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 16:34:10 2019

@author: Amarendra
"""

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import requests
from bs4 import BeautifulSoup
import time 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
##print(voices[1].id)

engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet_me():
    hour = int(datetime.datetime.now().hour)
    list_words = ["beautiful","graceful","marvelous","wonderful"]
    if hour>=0 and hour<12:
        speak('Hi Amar! Good Morning. \nThis is such a '+list_words[random.randint(0,len(list_words)-1)]+' day today. What can i do for you?')

    elif hour>=12 and hour<18:
        speak('Hi Amar, Good Afternoon.\nThis is such a '+list_words[random.randint(0,len(list_words)-1)]+' day today. What can i do for you?')

    else:
        speak('Hello Amar, Good Evening.\nThis is such a '+list_words[random.randint(0,len(list_words)-1)]+' day today. What can i do for you?')

#    speak('i am SUPER BOT')

def takeCommand():
    r = sr.Recognizer()
    r.energy_threshold=5000
    
    with sr.Microphone() as source:
        print('Listening.....')
       ## r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing.....')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        print(e)
        speak('Pardon ! can you say that again ?')
        return 'None'
    return query

r = sr.Recognizer()    

if __name__=="__main__":
    greet_me()

    while True:
        query = takeCommand().lower()

    ## logic that we will use to execute task
    
        if 'create incident' in query:
            speak("Kindly elaborate your issue")
#            audio2 = r.listen(source)
#            txt2 = r.recognize_google(audio2)
            query1 = takeCommand().lower()
            
            while query1 == 'none':
                query1 = takeCommand().lower() 
                  
                 
            else:
                                         
                        
                speak("Creating SNOW incident with short description"+query1)
                time.sleep(5)
                url="https://dev86028.service-now.com/api/now/table/incident"
                user='abel.tuter'
                password='Snow@123'
                headers={"Content-type":"application/json","Accept":"application/json"}
                response=requests.post(url, auth=(user,password) , headers=headers , data='{"short_description":"'+query1+'","impact":"1"}')
                inc = response.json()
                incNumber = inc['result']['number']
                speak("Created incident in ServiceNow with number"+incNumber)
                
    
    
    
        elif 'wikipedia' in query:
            speak('looking up for the query in wikipedia....')
            query = query.replace("Wikipedia",'')
            results = wikipedia.summary(query,sentences=2) 
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'temperature' in query:
            
            query = query.replace("temperature",'')
            city=query
            html= requests.request('GET',"https://www.google.com/search?q={0}+temp".format(city)).content
            soup=BeautifulSoup(html,"html.parser")
            print('Place:' +soup.find('span',{'class': 'tAd8D'}).text)
            speak('Place:' +soup.find('span',{'class': 'tAd8D'}).text)
            print('Temperature:' +soup.find('div',{'class': 'BNeawe'}).text)
            speak('Temperature:' +soup.find('div',{'class': 'BNeawe'}).text)
            print('' +soup.find('div',{'class': 'BNeawe tAd8D AP7Wnd'}).text)
            speak('' +soup.find('div',{'class': 'BNeawe tAd8D AP7Wnd'}).text)
            
        
#        elif "what is the temperature in" in query:
#            query = query.split(" ")
#            location = ""
#            for i in range(5,len(query)):
#                location = location+" "+query[i]
#                speak("Hold on, I will show you the temperature in" + location)
#                html = requests.request("GET","https://www.google.com/search?q=temperature+in+{0}".format(location)).content
#                soup = BeautifulSoup(html, "html.parser")
#                speak("The current temperature in "+soup.find("span",{"class":"tAd8D"}).text+ " is: "+soup.find("div",{"class":"BNeawe"}).text)
#            
            
        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open('youtube.com')
            
        elif 'open google' in query:
            speak('opening google')
            webbrowser.open('google.in')
            
        elif 'open stackoverflow' in query:
            speak('opening stackoverflow')
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            music_dir = r"E:\Music"
            songs = os.listdir(music_dir)
            print(songs)
            ran_num = random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir,songs[ran_num]))

        elif 'what time is it' in query:
            new_line = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'the time is {new_line}')
            
        elif "play the song" in query:
            song_list = query.split(" ")
            song=""
            for i in range(3,len(song_list)):
                song = song+" "+song_list[i]
                speak("Hold on, I will play"+song)
                html = requests.request("GET","https://www.youtube.com/results?search_query={0}".format(song)).content
                soup = BeautifulSoup(html, "html.parser")
                tag = soup.find("a",{"class":"yt-uix-sessionlink spf-link"})
                video_link = (tag.attrs["href"])
                webbrowser.open("https://www.youtube.com"+video_link)
                
        elif "how are you" in query:
            speak("I am fine, thanks for asking")
            
        elif "what can you do" in query:
            speak("I am unperfected right now, but.\nI can tell you the current time.\nI can tell you the temperature in any city.\nI can play you a song.")
            
        elif "thank you" in query:
            speak("Glad to help, you're welcome, goodbye")
            break

        
#