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
    is_positve = '0'
    #sent = tk.tokenize(sent)
    #print(sent)
    tagged_sent = tagger.tag(sent)
    #print(tagged_sent)
    for words in range(0, len(tagged_sent)-1):
        current_word = tagged_sent[words][0]
        current_tag = tagged_sent[words][1]
        next_word = tagged_sent[words+1][0]
        next_tag = tagged_sent[words+1][1]
        if( current_tag == 'NNP' or current_tag == 'NNPC'):
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

        elif (current_tag == 'PRP'):
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

