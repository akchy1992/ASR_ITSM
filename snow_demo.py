# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 13:46:18 2019

@author: Amarendra
"""

import pyttsx3
import requests
import speech_recognition as sr
import time 
#import json 
import os

#import pip._internal 
#print(pip._internal.pep425tags.get_supported())

engine = pyttsx3.init()

r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    engine.say("Welcome! How may I assist you?")
    engine.runAndWait()
    audio = r.listen(source)
    txt = r.recognize_google(audio)
    print(txt)
    if(txt.find('create incident') != -1):
        engine.say("Kindly elaborate your issue")
        engine.runAndWait()
        audio2 = r.listen(source)
        txt2 = r.recognize_google(audio2)
        print(txt2)
        engine.say("Creating SNOW incident with short description"+txt2)
        engine.runAndWait()
        time.sleep(5)
        url="https://dev86028.service-now.com/api/now/table/incident"
        user='abel.tuter'
        password='Snow@123'
        headers={"Content-type":"application/json","Accept":"application/json"}
        response=requests.post(url, auth=(user,password) , headers=headers , data='{"short_description":"'+txt2+'"}')
        inc = response.json()
        incNumber = inc['result']['number']
        engine.say("Created incident in ServiceNow with number"+incNumber)
        engine.runAndWait()
        
        
    if(txt.find('open Notepad') != -1):
        engine.say("Kindly wait, opening notepad!!")
        engine.runAndWait()
        time.sleep(3)
        os.system("notepad.exe")
        
#        
        