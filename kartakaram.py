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
# parser = Parser(lang='hin')

counter = 0


verbname = ['है', 'होना', 'खरीदा', 'दिया', 'उठाया', 'बढा', 'खर्चा', 'ढूंढा', 'भुगतान', 'उगाया', 'जा', 'खेला', 'ला', 'काटा', 'काम', 'बेचा', 'खरीदना', 'रखा', '*', 'बनाया', '*', 'पकडा', 'परोसा', 'कमाया', 'उधार', 'बचाया', 'मिला', 'जा', 'उपस्थित', 'देखा', 'रखा', 'खाया', 'कीमत', 'जीता', 'हारा', 'किया', 'किराया', 'ज़रूरत', 'लिया', 'खड़ा', 'खतम', 'डालना', 'बुलाया', 'तोडा', 'चमका', 'रखना', 'शुरु', 'बाटना', 'आना', 'भरना', 'साफ', 'जोड़ना', 'हार', 'टूटना', 'निशचित', 'फटना', 'शुरु', 'खतम', 'इकठ्ठा', 'ज़रूरत',
            'चाहना', '*', 'पूछना', 'नियंत्रित', 'शामिल', 'भार', 'इस्तमाल', 'चल', 'बनाना', 'बारिश', 'भागा', 'दौडा', 'टपकना', 'पीना', 'चढ़ना', 'फसल', 'दौडा', 'उतरना', 'इकठ्ठा', 'डालना', 'रंगना', 'बाकी', 'वापस', 'नापा', 'देखा', 'गिराना', 'हिलाना', 'जोडा', '*', '*', 'ढकना', 'कमना', 'बढाना', '*', 'झेलना', 'खिलाना', 'पढना', 'ठीक', 'बनाना', 'जाना', 'स्वामित्व', '*', 'बसना', 'अंकित', 'बोना', 'देना', 'जीना', 'उठाना', '*', 'गोद', 'चलाना', '*', 'परिणाम', 'खरीदना', 'खरीदना', 'ज़रुरत', 'घूमना', 'भागना', 'दौडना', 'फाडना']
verbtype = ['0', '0', 't+', 't-', 't+', '+', '--', '+', 't-', 't-', '+', '+', 't+', '--', '+', 't-', 't+', 't-', '-', '++', 't+', '+', '-', '+', 't+', '+', 't+', 't-', '+', '+', 't-', '--', '-', '+', '-', '1', 't+', '+', 't+', '+', '+', 't-', '+', '--', '+', 't-', '0', '-', '+', 't-', '+', '++', '-', '-', '+', '-', '+', '+',
            '++', '+', '+', '+', '+', '0', '0', '+', '--', '+', '++', '+', '+', '+', '--', '--', '+', 't+', '+', '+', '++', 't-', '+', '0', 't-', '+', '--', 't-', '+', '+', '+', '+', '+', '--', '++', '+', '+', 't-', '+', '++', '++', '+', '0', 't-', '+', '+', 't-', 't-', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '-']


def kartafunc(sentence):
    noun = [], tagg = []
    flag = 0
    karta = null, karma = null, recepient = null
    for words in sentence:
        tags = tagger.tag(words.split())
        if(tags[0][1] == 'NN' or tags[0][1] == 'NNP' or tags[0][1] == 'NNS'):
            ind = sentence.index(words)
            if(sentence[ind+1] == 'ने'):
                karta = words
            elif(sentence[ind+1] == 'को'):
                recepient = words
            elif(tagger.tag(sentence[ind-1]) == 'QF'):
                karma = words

        elif (tags[0][1] == 'PRP'):
            os.system("touch output.txt")
            f = open('tempfile.txt', 'w+', encoding='utf-8')
            flag = 0
            f.write(tags[0][0])
            os.system(
                "python3 run_morph_on_file_with_raw_text.py --input tempfile.txt --output output.txt")
            f2 = open('output.txt', 'r', encoding='utf-8')
            data = f2.read()
            os.system("rm output.txt")
            if(data.__contains__('ne')):
                karta = words
            elif(data.__contains__('ko')):
                recepient = words
    print(karta, karma, recepient)
