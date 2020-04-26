from __future__ import unicode_literals
from source import sentences, source
from isc_tokenizer import Tokenizer
from isc_tagger import Tagger
from isc_parser import Parser
import math

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
<<<<<<< HEAD

            
=======
c_values = []
counter_eq = 0


def eq_builder(karta, karma, verb_type, value, sampradaan):

    if verb_type == '0':
        values = []
        is_karta_present = False
        is_karma_present = False
        location_karta = 0
        location_karma = 0
        for c_value in c_values:
            if c_value[0] == karta:
                is_karta_present = True
                values.append(int(location_karta))
            location_karta += 1

        if is_karta_present:
            for location in values:
                if c_values[location][2] == karma:
                    is_karma_present = True
                    break
                location_karma += 1

        if is_karta_present and is_karma_present:
            c_values[values[location_karma]] = [karta, int(value), karma]
        else:
            c_values.append([karta, int(value), karma])
    
    if verb_type == '+':
        values = []
        is_karta_present = False
        is_karma_present = False
        location_karta = 0
        location_karma = 0
        for c_value in c_values:
            if c_value[0] == karta:
                is_karta_present = True
                values.append(int(location_karta))
            location_karta += 1

        if is_karta_present:
            for location in values:
                if c_values[location][2] == karma:
                    is_karma_present = True
                    break
                location_karma += 1

        if is_karta_present and is_karma_present:
            present = c_values[values[location_karma]][1] 
            c_values[values[location_karma]] = [karta, present + int(value), karma]
        else:
            c_values.append([karta, int(value), karma])
>>>>>>> a6a90bce1ca6cf0ef038eee5b968fc966658f965
        
    if verb_type == '-':
        values = []
        is_karta_present = False
        is_karma_present = False
        location_karta = 0
        location_karma = 0
        for c_value in c_values:
            if c_value[0] == karta:
                is_karta_present = True
                values.append(int(location_karta))
            location_karta += 1

        if is_karta_present:
            for location in values:
                if c_values[location][2] == karma:
                    is_karma_present = True
                    break
                location_karma += 1

        if is_karta_present and is_karma_present:
            present = c_values[values[location_karma]][1] 
            c_values[values[location_karma]] = [karta, present - int(value), karma]
        else:
            c_values.append([karta, int(value), karma])
        
    if verb_type == 't+':
        values = []
        values_s = []
        is_karta_present = False
        is_karma_present_1 = False
        is_karma_present_2 = False
        is_sampradaan_present = False
        location_karta = 0
        location_karma_1 = 0
        location_karma_2 = 0
        location_sampradaan = 0

        for c_value in c_values:
            if c_value[0] == karta:
                is_karta_present = True
                values.append(int(location_karta))
            if c_value[0] == sampradaan:
                is_sampradaan_present = True
                values_s.append(int(location_sampradaan))
            location_karta += 1
            location_sampradaan += 1

        if is_karta_present:
            for location in values:
                if c_values[location][2] == karma:
                    is_karma_present_1 = True
                    break
                location_karma_1 += 1
        if is_sampradaan_present:
            for location in values_s:
                if c_values[location][2] == karma:
                    is_karma_present_2 = True
                    break
                location_karma_2 += 1

        if is_karta_present and is_karma_present_1 and is_karma_present_2 and is_sampradaan_present:
            present_1 = c_values[values[location_karma_1]][1]
            present_2 = c_values[values_s[location_karma_2]][1] 
            c_values[values[location_karma_1]] = [karta, present_1 + int(value), karma]
            c_values[values_s[location_karma_2]] = [sampradaan, present_2 - int(value), karma]
        elif is_karta_present and is_karma_present_1:
            present_1 = c_values[values[location_karma_1]][1]
            c_values[values[location_karma_1]] = [karta, present_1 + int(value), karma]
            c_values.append([sampradaan, -1*int(value), karma])
        elif is_karma_present_2 and is_sampradaan_present:
            present_2 = c_values[values_s[location_karma_2]][1]
            c_values[values_s[location_karma_2]] = [sampradaan, present_2 - int(value), karma]
            c_values.append([karta, int(value), karma])
        else:
            c_values.append([karta, int(value), karma])
            c_values.append([sampradaan, -1*int(value), karma])

    if verb_type == 't-':
        values = []
        values_s = []
        is_karta_present = False
        is_karma_present_1 = False
        is_karma_present_2 = False
        is_sampradaan_present = False
        location_karta = 0
        location_karma_1 = 0
        location_karma_2 = 0
        location_sampradaan = 0

        for c_value in c_values:
            if c_value[0] == karta:
                is_karta_present = True
                values.append(int(location_karta))
            if c_value[0] == sampradaan:
                is_sampradaan_present = True
                values_s.append(int(location_sampradaan))
            location_karta += 1
            location_sampradaan += 1

        if is_karta_present:
            for location in values:
                if c_values[location][2] == karma:
                    is_karma_present_1 = True
                    break
                location_karma_1 += 1
        if is_sampradaan_present:
            for location in values_s:
                if c_values[location][2] == karma:
                    is_karma_present_2 = True
                    break
                location_karma_2 += 1

        if is_karta_present and is_karma_present_1 and is_karma_present_2 and is_sampradaan_present:
            present_1 = c_values[values[location_karma_1]][1]
            present_2 = c_values[values_s[location_karma_2]][1] 
            c_values[values[location_karma_1]] = [karta, present_1 - int(value), karma]
            c_values[values_s[location_karma_2]] = [sampradaan, present_2 + int(value), karma]
        elif is_karta_present and is_karma_present_1:
            present_1 = c_values[values[location_karma_1]][1]
            c_values[values[location_karma_1]] = [karta, present_1 - int(value), karma]
            c_values.append([sampradaan, int(value), karma])
        elif is_karma_present_2 and is_sampradaan_present:
            present_2 = c_values[values_s[location_karma_2]][1]
            c_values[values_s[location_karma_2]] = [sampradaan, present_2 + int(value), karma]
            c_values.append([karta, -1*int(value), karma])
        else:
            c_values.append([karta, -1*int(value), karma])
            c_values.append([sampradaan, int(value), karma])
            
        

<<<<<<< HEAD
=======

>>>>>>> a6a90bce1ca6cf0ef038eee5b968fc966658f965
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
    objects = []                                                            # Common Nouns
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
            elif((current_tag == 'NN' or current_tag == 'NNS' or current_tag == 'NNC') and is_number):
                concat_string = store_adj + " " + current_word
                objects.append(concat_string)
                store_adj = ""
                is_number = False
    
    print(i)
    print(containers)
    print(values)
    print(objects)