from __future__ import unicode_literals
from source import sentences, source
from isc_tokenizer import Tokenizer
from isc_tagger import Tagger
from isc_parser import Parser

tk = Tokenizer(lang='hin', split_sen=True)                                  # ensures the question is split according to sentences
tagger = Tagger(lang='hin')
parser = Parser(lang='hin')

counter = 0

for i in sentences:
    sep_sentence = tk.tokenize(i)                                           #  Stores the list of seperated sentences within a question
    counter += 1
    if(counter == 3):
        break
    tag_sep_sent = []                                                       # Stores the corresponding tags
    for j in sep_sentence:
        tag_sep_sent.append(tagger.tag(j))
    containers = []                                                         # Proper Nouns
    values = []                                                             # Numbers
    objects = []                                                            # Common Nouns
    for j in range(0, len(sep_sentence)):
        current_sent = sep_sentence[j]
        current_tagset = tag_sep_sent[j]
        is_number = False
        for k in range(0, len(current_tagset)):
            current_word = current_sent[k]
            current_tag = current_tagset[k][1]
            if(current_word == "$"):                                        # Handles special case: Money
                objects.append("$")
                continue
            if(current_tag == 'QC'):                                        
                if( current_word.isnumeric()):                      
                    values.append(current_word)
                    is_number = True
            elif(current_tag == 'NNP' or current_tag == 'NNPC'):
                containers.append(current_word)
            elif((current_tag == 'NN' or current_tag == 'NNS') and is_number):
                objects.append(current_word)
                is_number = False
    
    print(i)
    print(containers)
    print(values)
    print(objects)