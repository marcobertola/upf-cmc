#!/usr/bin/env python3

from asr import asr
#from asr import * as asr
import argparse
from osc import osc_client as osc 
from words2midi import w2midi
#from logic.logic import *
#from nl import nlp_context
#from nl.nlp import *

# 0 == Google Cloud Speech
# 1 == Sphinx
# 2 == Google Speech Recognition
ASR_MODE = 2	
DEBUG = False


def main():
    parser = argparse.ArgumentParser(description='Assistant parameters')
    parser.add_argument('--asr', action='store_true')
    args = parser.parse_args()
     
    #todo: making a loop 

    while True:
        if args.asr:
        	input_text = asr.processASR(ASR_MODE)
     
        else:
        	input_text = input("ask:")

        #splitting the sentence into single words
        input_words = input_text.split(' ')
        
        #calculating the distance between the words
        #todo: decide if we want a diatance between a defined numbers of words or different
        dist = w2midi.difference_word(input_words, len(input_words))

        #sending distance values to osc server
        #todo: decide how to send the sum of ditances
        osc.sendValues(dist)


if __name__ == "__main__":
    main()
