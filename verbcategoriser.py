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

for i in sentences:
    # Stores the list of seperated sentences within a question
    sep_sentence = tk.tokenize(i)
    # Stores the corresponding tags
    tag_sep_sent = []
    values = []
    containers = []
    objects = []
    for j in sep_sentence:
        for words in j:
            # print(words)
            tags = tagger.tag(words.split())
            # print(tags)
            # tags[0] = tags[0].split()
            if(tags[0][1] == 'VM'):
                f = open('tempfile.txt', 'w+', encoding='utf-8')
                flag = 0
                f.write(tags[0][0])
                os.system(
                    "python run_morph_on_file_with_raw_text.py --input tempfile --output output.txt")
                f.close()
                f2 = open('output.txt', 'r', encoding='utf-8')
                data = f2.read()
                data = data.replace(',', ' ')
                data = data.replace("'", ' ')
                data = data.split()
                l = len(data)
                for x in range(l):
                    if(data[x] == "af="):
                        stem = data[x+1]
                        if(stem in verbname):
                            ind = verbname.index(stem)
                            print(verbtype[ind])
                            flag = 1
                            break
                if flag == 0:
                    print("*")
                f2.close()
