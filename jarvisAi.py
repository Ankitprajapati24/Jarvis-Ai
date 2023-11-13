import speech_recognition as sr
import os
import win32com.client


speaker = win32com.client.Dispatch("SAPI.SpVoice")

while 1:
    print("Jarvis Ai is availavle for you !!")
    print("Now in put here : ")
    s = input()
    print("not taking the input")
    
    speaker.Speaker(s)
