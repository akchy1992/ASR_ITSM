# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 20:42:07 2019

@author: Amarendra
"""

import requests
from gtts import gTTS
from pygame import mixer
import speech_recognition as sr

r=sr.Recognizer()
mic=sr.Microphone()

with mic as source:
    
    r.adjust_for_ambient_noise(source, duration=1)
#    tts = gTTS(text="Elaborate your issue", lang= 'en')
#    tts.save('response67.mp3')
    mixer.music.load('response52.mp3')
    mixer.music.play()
    
    audio=r.listen(source, phrase_time_limit=5)
    text=r.recognize_google(audio)
    print(text)

    if(text.find('yes') != -1):
        mixer.music.load('response67.mp3')
        
        mixer.music.play()
        audio2= r.listen(source,phrase_time_limit=5)
        text2=r.recognize_google(audio2)
        tt = gTTS(text="creating incident with description"+text2,lang='en')
        tt.save('so.mp3')
        mixer.music.load('so.mp3')
        mixer.music.play()
        print(text2)
        url="https://dev30796.service-now.com/api/now/table/incident"
        user='abel.tuter'
        password='Snow@123'
        headers={"Content-type":"application/json","Accept":"application/json"}
        response=requests.post(url, auth=(user,password) , headers=headers , data='{"short_description":"'+text2+'"}')
        print(response.status_code)
    #        print("say")      
#    tts = gTTS(text="Say Something", lang='en')
#    tts.save('response5.mp3')
#    mixer.music.load('response5.mp3')
#    mixer.music.play()
#     audio=r.listen(source)
#     text= r.recognize_google(audio)
#        
#    print(text)
##        
#        if(text.find(substring)):
#            print(text)
#            url="https://dev30796.service-now.com/api/now/table/incident"
#            user='abel.tuter'
#            password='Snow@123'
#            headers={"Content-type":"application/json","Accept":"application/json"}
#            response = requests.post(url, auth=(user,password) , headers=headers , data='{"short_description":"'+text+'"}')
#            print(response.status_code)
#    except sr.UnknownValueError:
#        print("Sphinx could not understand audio")
#    except sr.RequestError as e:
#        print("Sphinx error; {0}".format(e))