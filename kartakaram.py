# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from source import source, sentences
from isc_tokenizer import Tokenizer
from isc_tagger import Tagger
import os
from os import system

# ensures the question is split according to sentences
tk = Tokenizer(lang='hin', split_sen=True)
tagger = Tagger(lang='hin')

counter = 0

def kartafunc(sent):
    karta = 0
    karma = 0
    recepient = 0
    is_positve = '0'
    tagged_sent = tagger.tag(sent)
    for words in range(0, len(tagged_sent)-1):
        current_word = tagged_sent[words][0]
        current_tag = tagged_sent[words][1]
        next_word = tagged_sent[words+1][0]
        next_tag = tagged_sent[words+1][1]
        if( current_tag == 'NNP' or current_tag == 'NNPC'):                 # gets subject and object of sentence by identifying case markers
            if(next_word == 'ने'):
                karta = current_word
            elif(next_word == 'को'):
                recepient = current_word
                is_positve = 't+'
            elif(next_word == 'से'):
                recepient = current_word
                is_positve = 't-'
        if(current_tag == 'QC'):
            if(next_tag == 'JJ'):
                if(tagged_sent[words+2][1] == 'NN' or tagged_sent[words+2][1] == 'NNP' or tagged_sent[words+2][1] == 'NNS' or tagged_sent[words+2][1] == 'NNPC'):
                    karma = next_word + " " + tagged_sent[words+2][0]
            elif(next_tag == 'NN' or next_tag =='NNP' or next_tag == 'NNPC' or next_tag == 'NNS'):
                karma = next_word

        elif (current_tag == 'PRP'):                                        # in case case markers are used as morphemes
            os.system("touch output.txt")
            f = open('tempfile.txt', 'w+', encoding='utf-8')
            f.write(current_word)
            os.system(
                "python3 run_morph_on_file_with_raw_text.py --input tempfile.txt --output output.txt")
            f2 = open('output.txt', 'r', encoding='utf-8')
            data = f2.read()
            os.system("rm output.txt")
            if(data.__contains__('ne')):
                karta = current_word
            elif(data.__contains__('ko')):
                recepient = current_word
                is_positve = 't+'
            elif(data.__contains__('se')):
                recepient = current_word
                is_positve = 't-'
    l = []
    if( karta == karma or karta == recepient or karma == recepient):
        return [0,0,0,'0']
    l.append(karta)
    l.append(karma)
    l.append(recepient)
    l.append(is_positve)
    return l

