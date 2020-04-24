from __future__ import unicode_literals
from source import sentences, source
from isc_tokenizer import Tokenizer
from isc_tagger import Tagger
from isc_parser import Parser
import math
from kartakaram import kartafunc
from verbcategoriser import categorise
from calculate import eq_build, c_values

tk = Tokenizer(lang='hin', split_sen=True)                                  # ensures the question is split according to sentences
tagger = Tagger(lang='hin')
parser = Parser(lang='hin')

counter = 0
x = []
x.append('राज के पास 4 नीला बॉल और 6 हरा बॉल थे। राज ने हैरी को 3 नीला बॉल्स दिए। राज के पास कितनी नीला गेंदें हैं?')

'''
The function takes in parameters. 
You need to change two things.
two different types are there in the function.
First kind are non-transfer
How I have dealt with it is if it is the first time we are appending append as needed.
else i find where it already exists and make the required changes. You can read the code with variables to understand it better
for transfer 
the extra paramter the recepient is also required
so i do the same thing as above but change the values for the recepient too

what changes you need to make:
1) make it only a list of lists or a list of list of lists (do not try this pls)
2) in the list make sure you add another element in the lists which takes in the karta as input too.
3) suppose karta exists do the same shit, else append accordingly 
4) else add the new karta with the required elements ig
5) if it is not a transfer, let the recepeint be the string 'none' when testing. Not that it matters but standardized
Happy coding :) 
'''

counter_eq = 0
        
y = []
y.append(sentences[37])
#print(source[37][1])

for i in y:
    sep_sentence = tk.tokenize(i)                                           #  Stores the list of seperated sentences within a question
    counter += 1
    if(counter == 2):
        break
    tag_sep_sent = []                                                       # Stores the corresponding tags
    for j in sep_sentence:
        tag_sep_sent.append(tagger.tag(j))
    print(tag_sep_sent)
    containers = []                                                         # Proper Nouns
    values = []                                                             # Numbers
    objects = []                                                            # Common Nouns
    assign = []																# Container, Value, Adjective, Object
    is_transfer = False


    for j in range(0, len(sep_sentence)):
        current_sent = sep_sentence[j]
        current_tagset = tag_sep_sent[j]
        is_number = False
        store_adj = ""                                                      # Stores the adjective assosciated with a object
        store_last_proper = ""                                              # Stores the required proper noun, which is the first to the right of QC
        verb_list = []
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
            
            if(current_word == "$"):                                        # Handles special case: Money
                objects.append("$")
                continue
            if(current_tag == 'JJ' and (next_tag == 'NN' or next_tag == 'NNS' ) and is_number):
                store_adj = current_word
                continue
            if(current_tag == 'QC'):                    
                if( current_word[0].isnumeric()):                      
                    values.append(current_word)
                    is_number = True
                    containers.append(store_last_proper)
            elif(current_tag == 'NNP' or current_tag == 'NNPC' or current_tag == 'PRP'):
                store_last_proper = current_word                           # stores the last proper noun before the quantifier
            elif((current_tag == 'NN' or current_tag == 'NNS') and is_number):
                concat_string = store_adj + " " + current_word
                objects.append(concat_string)
                r = [store_last_proper, values[len(values)-1], concat_string]
                assign.append(r)
                store_adj = ""
                is_number = False
            elif(current_tag == 'VM'):
                verb_type  = categorise(current_word)
                print(verb_type)
                if(verb_type != '0' and is_transfer == False):
                    is_transfer = True
                

    print(i)
    print(containers)
    print(values)
    print(objects)
    print(assign)



