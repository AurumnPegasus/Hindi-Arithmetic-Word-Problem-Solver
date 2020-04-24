from __future__ import unicode_literals
from source import sentences, source
from isc_tokenizer import Tokenizer
from isc_tagger import Tagger
import math
from kartakaram import kartafunc
from verbcategoriser import categorise
from calculate import eq_build, c_values

# ensures the question is split according to sentences
tk = Tokenizer(lang='hin', split_sen=True)
tagger = Tagger(lang='hin')


def finalsent(sent, assign, is_transfer):
    nouns = []
    tagged_sent = tagger.tag(sent)
    foundcont = 0
    foundobj = 0
    qf_flag = 0
    # print(tagged_sent)
    if is_transfer == True:
        for words in tagged_sent:
            if words[1] == 'NN' or words[1] == 'NNP' or words[1] == 'NNS' or words[1] == 'NNPC' or words[1] == 'PRN':
                nouns.append(words[0])
                if qf_flag == 1:
                    foundobj = words[0].strip()
                    break
            elif words[1] == 'QF':
                foundcont = nouns[-1]
                qf_flag = 1
        for elem in assign:
            elem[0] = elem[0].strip()
            elem[2] = elem[2].strip()
            if(elem[0] == foundcont and elem[2] == foundobj):
                print(float(elem[1]))
                return float(elem[1])
        sum = 0
        for elem in assign:
            elem[2] = elem[2].strip()
            if(elem[2] == foundobj):
                sum = sum + float(elem[1])
        print(sum)
        return sum
    else:
        operation = '+'  # taking + to be default op
        for words in tagged_sent:
            if(words[0] == 'कुल' or words[0] == 'मिलकर' or words[0] == 'मिलाकर'):
                operation = '+'
                break
            if words[0] == 'पहले' or words[0] == 'पेहले' or words[0] == 'ज़्यादा' or words[0] == 'ज्यादा':
                operation = '-'
                break
        for words in tagged_sent:
            if words[1] == 'QF':
                qf_flag = 1
            if (words[1] == 'NN' or words[1] == 'NNP' or words[1] == 'NNS' or words[1] == 'NNPC' or words[1] == 'PRP') and qf_flag == 1:
                foundobj = words[0].strip()
                break
        sum = 0
        if operation == '-':
            firstelemflag = 0
            for elem in assign:
                elem[2] = elem[2].strip()
                if(elem[2] == foundobj):
                    if firstelemflag == 0:
                        sum = sum + float(elem[1])
                        firstelemflag = 1
                    else:
                        sum = sum - float(elem[1])
            print(sum)
            return sum
        else:
            sum = 0
            for elem in assign:
                elem[2] = elem[2].strip()
                if(elem[2] == foundobj):
                    sum = sum + float(elem[1])
            print(sum)
            return sum
