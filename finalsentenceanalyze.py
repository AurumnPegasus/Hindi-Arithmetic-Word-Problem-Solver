from __future__ import unicode_literals
from source import sentences, source
from isc_tokenizer import Tokenizer
from isc_tagger import Tagger
import math
from kartakaram import kartafunc

# ensures the question is split according to sentences
tk = Tokenizer(lang='hin', split_sen=True)
tagger = Tagger(lang='hin')


def finalsent(sent, assign, is_transfer, default_change):
    container = []
    positive = ['कुल', 'मिलकर', 'मिलाकर', 'अखंडित']
    negative = ['पहले','पेहले', 'ज़्यादा', 'ज्यादा', 'बाकी', 'खर्च', 'खरीदीं', 'बच', 'खरीदी', 'बची']
    tagged_sent = tagger.tag(sent)
    foundcont = "*"
    foundobj = "*"
    got_adj = ""
    qf_flag = 0
    got_one = False
    if is_transfer == True:                                                 # there is a transfer occuring
        for index in range(0, len(tagged_sent)-1):
            current_word = tagged_sent[index][0].strip()
            current_tag = tagged_sent[index][1] 
            next_word = tagged_sent[index+1][0].strip()
            next_tag = tagged_sent[index+1][1]
            if current_tag == 'NNP' or current_tag == 'NNPC' or current_tag == 'PRP':
                container.append(current_word)
            if current_tag == 'JJ':
                if next_tag == 'NN' or next_tag == 'NNP' or next_tag == 'NNS' or next_tag == 'NNPC':
                    if qf_flag == 1:
                        foundobj = current_word + " " + next_word
                        break
            if current_tag == 'NN' or current_tag == 'NNP' or current_tag == 'NNS' or current_tag == 'NNPC':
                if qf_flag == 1:
                    foundobj = current_word.strip()        
                    break
            elif current_tag == 'QF':
                qf_flag = 1
                foundcont = container[len(container)-1].strip()
        for elem in assign:
            elem[0] = elem[0].strip()                                      # have to make it container specific
            elem[2] = elem[2].strip()
            if(elem[0].endswith(foundcont) and elem[2].endswith(foundobj)):
                return float(elem[1])
        sum = 0
        for elem in assign:
            elem[2] = elem[2].strip()
            if(elem[2].endswith(foundobj)):
                sum = sum + float(elem[1])
        return sum
    else:
        operation = '+'                                                    # taking + to be default op
        if(default_change):
            operation = '-'
        for words in tagged_sent:
            if(default_change == False and got_one == False):               # if I havent already found out negative 
                for check in positive:
                    if words[0] == check:
                        operation = '+'
                        got_one = True
                        break           
            if(got_one == False):                                           # If I havent already found out positive
                for check in negative:
                    if(words[0] == check):
                        operation = '-'
                        break
        for words in tagged_sent:
            if words[0] == "$":
                foundobj = words[0].strip()
                break
            if words[1] == 'QF' or words[1] == 'WQ':
                qf_flag = 1
            if words[1] == 'JJ' and qf_flag == 1:
                got_adj = words[1]
            if (words[1] == 'NN' or words[1] == 'NNP' or words[1] == 'NNS' or words[1] == 'NNPC' or words[1] == 'PRP') and qf_flag == 1:
                foundobj = got_adj.strip() + " " + words[0].strip()
                break
        sum = 0
        have_answer = False
        foundobj = foundobj.strip()
        if operation == '-':
            firstelemflag = 0
            for elem in assign:
                elem[2] = elem[2].strip()                                   # object specific
                if(elem[2].endswith(foundobj)):
                    if firstelemflag == 0:
                        sum = sum + float(elem[1])
                        firstelemflag = 1
                        have_answer = True
                    else:
                        sum = sum - float(elem[1])
            if have_answer == False:                                        # cant find object, assume object of first item is the one
                foundobj = assign[0][2].strip()
                firstelemflag = 0
                for elem in assign:
                    elem[2] = elem[2].strip()
                    if(elem[2].endswith(foundobj)):
                        if firstelemflag == 0:
                            sum = sum + float(elem[1])
                            firstelemflag = 1
                            have_answer = True
                        else:
                            sum = sum - float(elem[1])
            return sum
        else:
            sum = 0
            for elem in assign:
                elem[2] = elem[2].strip()                                   # object specific
                if(elem[2].endswith(foundobj)):
                    sum = sum + float(elem[1])
                    have_answer = True
            if have_answer == False:                                        # cant find object, assume object of first item is the one
                foundobj = assign[0][2]
                for elem in assign:
                    elem[2] = elem[2].strip()
                    if(elem[2].endswith(foundobj)):
                        sum = sum + float(elem[1])
                        have_answer = True
            return sum
