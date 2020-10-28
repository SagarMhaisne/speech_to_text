# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 20:01:12 2020

@author: SM51998
"""

import speech_recognition as SRG
import time

store = SRG.Recognizer()
with SRG.Microphone() as s:
    print("Speak...")
    
    audio_input = store.record(s,duration=7)
    print("Recording Time : ",time.strftime("%I:%M:%S"))
    
    try:
        text_output = store.recognize_google(audio_input)
        print("Text converted from audio :\n")
        print(text_output)
        print("Finished !")
        print("Execution Time : ",time.strftime("%I:%M:%S"))
    except:
        print("Couldn't process the audio input.")