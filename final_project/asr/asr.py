#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class
# moneyball-1571579309592

import speech_recognition as sr
import os


def recognizeSphinx(r, audio):
    speech = ''
    try:
        speech = r.recognize_sphinx(audio)
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

    return speech


def recognizeGoogleSpeechRecognition(r, audio):
    speech = ''
    try:
        speech = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return speech


def recognizeGoogleCloudSpeech(r, audio):
    speech = ''
    try:
        speech = r.recognize_google_cloud(audio, credentials_json=getCredentials())
    except sr.UnknownValueError:
        print("Google Cloud Speech could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech service; {0}".format(e))

    return speech


def getCredentials():
    #json_path = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
    f = open("asr/keypath.txt", "r")
    json_path = f.readline().rstrip()
    with open(json_path, 'r') as file:
        google_cloud_speech_credentials = file.read()

    return google_cloud_speech_credentials


def processASR(asr_mode):
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

    speech = ''
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Say something!")
        audio = r.listen(source)
        if 0 == asr_mode:
            speech = recognizeGoogleCloudSpeech(r, audio)
        elif 1 == asr_mode:
            speech = recognizeSphinx(r, audio)
        else:
            speech = recognizeGoogleSpeechRecognition(r, audio)
        print(speech)


    return speech


def main():
    processASR()


if __name__ == "__main__":
    main()
