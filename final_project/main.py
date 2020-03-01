#!/usr/bin/env python3


from asr import asr
import argparse
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
    
      
    if args.asr:
    	input_text = asr.processASR(ASR_MODE)
    else:
    	input_text = input("ask:")


if __name__ == "__main__":
    main()
