import re
import ast

fn = open('./language-data/synonyms-vn.txt', 'r', encoding='utf8')
data = fn.read()

list_syn = ast.literal_eval(data)

fn = open('./language-data/intents-vn.txt', 'r', encoding='utf8')
data = fn.read()
intent_names = data.split('\n')

keywords = {}
keywords_dict = {}


for intent in intent_names:
    keywords[intent] = []
    for synonym in list(list_syn[intent]):
        keywords[intent].append('.*\\b' + synonym + '\\b.*')

for intent, keys in keywords.items():
    keywords_dict[intent] = re.compile('|'.join(keys))
# print(keywords_dict)

fn = open('./language-data/responses-vn.txt', 'r', encoding='utf8')
data = fn.read()

responses = ast.literal_eval(data)
# print(responses)
