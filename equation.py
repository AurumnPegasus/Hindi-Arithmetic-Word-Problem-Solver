from __future__ import unicode_literals
from source import sentences, source
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from isc_tokenizer import Tokenizer
from isc_tagger import Tagger
from isc_parser import Parser

tk = Tokenizer(lang='hin', split_sen=True)                                  # ensures the question is split according to sentences
tagger = Tagger(lang='hin')
parser = Parser(lang='hin')

counter = 0
x = []
x.append('राज के पास 4 भूरा बॉल और 6 हरा बॉल थे। राज ने हैरी को तीन ब्राउन बॉल्स दिए। राज के पास कितनी  भूरा गेंदें हैं?')

for i in x:
    sep_sentence = tk.tokenize(i)                                           #  Stores the list of seperated sentences within a question
    counter += 1
    if(counter == 5):
        break
    tag_sep_sent = []                                                       # Stores the corresponding tags
    for j in sep_sentence:
        tag_sep_sent.append(tagger.tag(j))
    print(tag_sep_sent)
    containers = []                                                         # Proper Nouns
    values = []                                                             # Numbers
    objects = []
    Noun_tags_1 = ['NNP', 'PRP', 'NNPC']
    Noun_tags_2 = [ 'NN', 'NNS']
    length = len(sep_sentence) #so that it is not calculated everytime                                                            # Common Nouns
    for j in range(0, length):
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
            if(current_word == "$"):                                        # Handles special case: Money
                objects.append("$")
                continue
            if(current_tag == 'JJ' and (next_tag == 'NN' or next_tag == 'NNS' ) and is_number):
                store_adj = current_word
                print(store_adj)
                continue
            if(current_tag == 'QC'):                                        
                if( current_word.isnumeric()):                      
                    values.append(current_word)
                    is_number = True
                    containers.append(store_last_proper)
            elif(current_tag == 'NNP' or current_tag == 'NNPC' or current_tag == 'PRP'):
                store_last_proper = current_word                           # stores the last proper noun before the quantifier
            elif((current_tag == 'NN' or current_tag == 'NNS') and is_number):
                concat_string = store_adj + " " + current_word
                objects.append(concat_string)
                store_adj = ""
            elif(current_tag == in Noun_tags_1):
                # if current_tagset[k-1][1] == 'JJ':
                #     containers.append(current_sent[k-1] + ' ' + current_word)
                # else:
                containers.append(current_word)
            elif(current_tag in Noun_tags_2 and is_number):
                if current_tagset[k-1][1] == 'JJ':
                    objects.append(current_sent[k-1] + ' ' + current_word)
                else:
                    objects.append(current_word)
                is_number = False
    
    print(i)
    print(containers)
    print(values)
    print(objects)