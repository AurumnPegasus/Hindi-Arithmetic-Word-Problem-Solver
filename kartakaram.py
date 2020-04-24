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


def kartafunc(sent):
    karta = 0
    karma = 0
    recepient = 0
    sent = "राम ने राज को 10 किताबें दीं"
    sent = tk.tokenize(sent)
    tagged_sent = tagger.tag(sent[0])
    for words in tagged_sent:
        if(words[1] == 'NN' or words[1] == 'NNP' or words[1] == 'NNS' or words[1] == 'NNPC'):
            print(words[0])
            ind = tagged_sent.index(words)
            if(tagged_sent[ind+1][0] == 'ने'):
                karta = words[0]
            elif(tagged_sent[ind+1][0] == 'को'):
                recepient = words[0]
            elif(tagged_sent[ind-1][1] == 'QC'):
                karma = words[0]

        elif (words[1] == 'PRP'):
            os.system("touch output.txt")
            f = open('tempfile.txt', 'w+', encoding='utf-8')
            f.write(words[0])
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

#print(sentences[18])
kartafunc(sentences[18])