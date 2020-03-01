#!/usr/bin/env python3


import pyttsx3
import os


class VoiceTTS:

    def __init__(self):
        if os.name == 'nt':
            self.engine = pyttsx3.init("sapi5", debug=False)
        else:
            self.engine = pyttsx3.init("nsss", debug=False)

    def processTextToSpeech(self, text):

        self.engine.say(text)
        self.engine.runAndWait()
