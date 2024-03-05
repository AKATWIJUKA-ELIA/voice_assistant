#!/usr/bin/python3

print("Checking for pyttsx3")
try:
    import pyttsx3
except ImportError:
    print("You should install pyttsx3 before continuing")

print("Checking for pywhatkit")
try:
    import pywhatkit
except ImportError:
    print("You should install pywhatkit before continuing")

print("Checking for wikipedia")
try:
    import wikipedia
except:
    print("You should install wikipedia before continuing")

print("Checking for speech_recognition ")
try:
    import speech_recognition
except:
    print("You should install speech_recognition before continuing")
