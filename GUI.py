# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 14:03:42 2019

@author: Manik
"""

#import tkinter as tk 
from tkinter import *
import os
image = []

#window= tk.Tk()
window = Tk()
window.title("Automatic Speech Recognition")
window.geometry('230x230')

def run():
    os.system("python C:/Users/Amarendra/Desktop/python/personal_ass.py")

btn = Button(window, text = 'click me', command=run)
img = PhotoImage(file="C:/Users/Amarendra/Desktop/python/images.png") # make sure to add "/" not "\"
btn.config(image=img)
btn.pack()
btn.grid(column=100,row=300)

window.mainloop()