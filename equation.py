from __future__ import unicode_literals
from source import sentences, source
from isc_tokenizer import Tokenizer
from isc_tagger import Tagger
from isc_parser import Parser
import math
from kartakaram import kartafunc
from finalsentenceanalyze import finalsent
from calculate import eq_builder

tk = Tokenizer(lang='hin', split_sen=True)                                  # ensures the question is split according to sentences
tagger = Tagger(lang='hin')
parser = Parser(lang='hin')

correct = 0
total = 0
negative = ['टूटे', 'खर्च', 'देने', 'नहीं', 'फटे']
wrong = []

y = []
for i in range(0,100):
    y.append(source[i])
    total +=1 


for i in y:
    sep_sentence = tk.tokenize(i[0])                                        #  Stores the list of seperated sentences within a question
    tag_sep_sent = []                                                       # Stores the corresponding tags
    for j in sep_sentence:
        tag_sep_sent.append(tagger.tag(j))
    containers = []                                                         # Proper Nouns
    values = []                                                             # Numbers
    objects = []                                                            # Common Nouns
    assign = []																# Container, Value, Adjective, Object
    is_transfer = False
    default_change = False
    came_here = False
    rem_size = 0

    for j in range(0, len(sep_sentence)):
        current_sent = sep_sentence[j]
        current_tagset = tag_sep_sent[j]
        is_number = False
        store_adj = ""                                                      # Stores the adjective assosciated with a object
        store_last_proper = ""                                              # Stores the required proper noun, which is the first to the right of QC
        
        for k in range(0, len(current_tagset)-1):   
            current_word = current_sent[k]
            current_tag = current_tagset[k][1]
            next_word = current_sent[k+1]
            next_tag = current_tagset[k+1][1]
            if(current_word[0].isnumeric()):
                current_tag = 'QC'
            if( next_word[0].isnumeric()):
                next_tag = 'QC'
            if(current_tag == 'PRP' and len(assign) != 0):
                current_word = assign[len(assign)-1][0]

            # handles special cases regarding when we have to subtract from a total given
            if((current_word == 'मिलकर' or current_word == 'मिलाकर' or current_word == "बाकी") and j==(len(sep_sentence)-1)):      
                rem_size = len(assign)
                came_here = True
            elif((current_word == 'मिलकर' or current_word == 'मिलाकर' or current_word == "बाकी" )):
                default_change = True
                came_here = True
            elif((current_word == "पहले" or current_word == "पेहले") and len(assign)>0):
                default_change = True
                came_here = True
            if(current_word == "$"):                                        # Handles special case: Money
                objects.append("$")
                values.append(next_word)
                concat_string = store_adj + " " + current_word
                change_sign = False
                for check in negative:                                      # check for negative verbs
                    if(check == current_sent[k+2]):
                        change_sign = True
                        break
                if(change_sign == True):
                    values[len(values)-1] = float(values[len(values)-1])*(-1)
                r = [store_last_proper, values[len(values)-1], concat_string]
                assign.append(r)
                store_adj = ""
                is_number = False
                continue
            # in case an adjective is there
            if(current_tag == 'JJ' and (next_tag == 'NN' or next_tag == 'NNS' or next_tag == 'NNP' ) and is_number):        
                store_adj = current_word
                continue
            if(current_tag == 'QC'):                    
                if( current_word[0].isnumeric()):                    
                    values.append(current_word)
                    is_number = True
                    containers.append(store_last_proper)                # getting the container
            elif((current_tag == 'NN' or current_tag == 'NNS' or current_tag == 'NNP') and is_number):
                concat_string = store_adj + " " + current_word
                objects.append(concat_string)
                change_sign = False
                if(next_tag == 'VM' or next_word =='नहीं'):
                    for check in negative:
                        if(check == next_word):
                            change_sign = True
                            break
                if(change_sign == True):
                    values[len(values)-1] = float(values[len(values)-1])*(-1)
                # storing the final instance as [ container name, value, object ]
                r = [store_last_proper, values[len(values)-1], concat_string]
                assign.append(r)
                store_adj = ""
                is_number = False
            elif(current_tag == 'NNP' or current_tag == 'NNPC' or current_tag == 'PRP'):
                store_last_proper = current_word                           # stores the last proper noun before the quantifier
            elif(current_tag == 'VM'):
                l = kartafunc(current_sent)                                 # check for transfer
                if(l[0] !=0 and l[1]!=0 and l[2]!=0):
                    is_transfer = True
                    temp = []
                    for index in range(0, len(assign)-1):
                        temp.append(assign[index])
                    assign = eq_builder(l[0], l[1], l[3], values[len(values)-1], l[2], temp)
                
        if(j==len(sep_sentence)-1):                                         # check for final sentence
            if(len(assign) != rem_size and came_here == True):
                default_change = True
            store_ans = finalsent(current_sent, assign, is_transfer, default_change)
            store_ans = abs(store_ans)
            actual_ans = float(i[1])
            print(store_ans)
            print(actual_ans)
            pr = 0.01
            diff = abs(actual_ans - store_ans)
            if diff<=pr:
                print("CORRECT")
                correct += 1
            else:
                print("WRONG")
                wrong.append((tag_sep_sent, assign, actual_ans, store_ans))

print(total)
print(correct)
acc = (correct)/(total)
print("ACCURACY ")
print(acc*100)
