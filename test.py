from __future__ import unicode_literals
from isc_tokenizer import Tokenizer
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from isc_parser import Parser
from isc_tagger import Tagger 
from source import sentences as sent
from source import source


tk = Tokenizer(lang='eng', smt=True, split_sen = True)
tagger = Tagger(lang='hin')
parser = Parser(lang='hin')

#Created an instance of all the sentences.
data = sent
zero = ['has', 'is']
checks = ['NNP', 'PRP', 'NNPC', 'NN', 'NNS']
#It is QF
# text = "एक वेज्ञानिक मेडिकल लेब में रक्त की जांच कर रहा था। 2 किस्सो में मिलाकर उसे 7341 रक्त कोशिकाए थी। पेहले किस्से में उन्हे 4221 कोशिकाए मिली, तो दूसरे में कितनी थी?"
# split_text = text.split('।')

#the split thing is gay. add  a space between word and . 
# text = "Darnel is walking 0.875 miles and he ran 0.75 miles . How many miles did he complete ?"
sentences = sent_tokenize(data)
ans = len(sentences)


# for sentence in sentences:
# 	tags = tagger.tag(sentence .split())
# 	for tag in tags:
# 		if tag[0] in zero:
# 			ans -= 1
# 			break
	
# ans = len(sentences) - ans - 1



for sentence in sentences:
	spl_sentence = tk.tokenize(sentence)
	nouns = []
	objects = []
	values = []
	subjects = []
	tags = tagger.tag(sentence[0] .split())
	length = len(tags)
	isnumber = False
	for i in range(length):
		if tags[i][1] in checks:
			if tags[i-1][1] == 'JJ':
				nouns.append(tags[i-1][0] + ' ' + tags[i][0])
			else:
				nouns.append(tags[i][0])
		if tags[i][1] == 'QC':
			values.append(tags[i][0])
			if tags[i+1][1] == 'JJ':
				objects.append(tags[i+1][0] + ' ' + tags[i+2][0])
			else:
				objects.append(tags[i+1][0])

	for noun in nouns:
		if noun in objects:
			continue
		else:
			subjects.append(noun)

	print(nouns)
	print(subjects)
	print(objects)
	print(values)
	break

