from __future__ import unicode_literals
from source import source
from isc_tokenizer import Tokenizer
from isc_tagger import Tagger
from isc_parser import Parser

tk = Tokenizer(lang='hin')
tagger = Tagger(lang='hin')
parser = Parser(lang='hin')

tokenized_source = []

for i in source:
    tokenized_source.append(tk.tokenize(i[0]))

tree = parser.parse(tokenized_source[70])
print('\n'.join(['\t'.join(node) for node in tree]))