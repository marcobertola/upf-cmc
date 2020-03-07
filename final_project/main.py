#!/usr/bin/env python3
#import sys
#sys.path.append('./asr' + 'asr')
from asr import asr
#from asr import * as asr
import argparse
from osc import osc_client as osc
from time import sleep
from words2midi import w2midi
import re
#from logic.logic import *
#from nl import nlp_context
#from nl.nlp import *

# 0 == Google Cloud Speech
# 1 == Sphinx
# 2 == Google Speech Recognition
ASR_MODE = 2	
DEBUG = False
START = 1
STOP = 0


def main():
    parser = argparse.ArgumentParser(description='Assistant parameters')
    parser.add_argument('--asr', action='store_true')
    parser.add_argument('-n', help='Number of words taken into account when creating the parameters for a single sound. Default n=2', default=2)
    args = parser.parse_args()
    n_words_sound = int(args.n)
    #instatntiation of osc client class
    osc_client = osc.OSCClient()

    while True:
        try:
            if args.asr:
                input_text = asr.processASR(ASR_MODE)
         
            else:
                print("#########################")
                input_text = input("ask:")

            #splitting the sentence into single words
            input_words = re.sub(r' +', ' ', input_text).strip().lower().split(' ')

            #sending starting trigger value
            osc_client.client.send_message("/trigger", START)

            #sending distances
            for idx in range(len(input_words) - n_words_sound + 1):
                
                group_words = input_words[idx:idx+n_words_sound]  # Calculate the distance for every combination of n-consecutive words
                print("Words: ", group_words)
                #calculating the distance between the words
                #todo: decide if we want a diatance between a defined numbers of words or different
                dist = w2midi.difference_word(group_words, len(group_words))
                #sending distance values to osc server
                #todo: decide how to send the sum of ditances
                osc_client.sendValues(dist)
                sleep(0.2)

            #sending stop trigger value
            osc_client.sendTriggerValue(STOP)

        except Exception as e:
            print("Exception: ")
            print(str(e))
            print("Program continues...")


if __name__ == "__main__":
    main()
