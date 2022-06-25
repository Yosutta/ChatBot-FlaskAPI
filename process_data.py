import re
import ast

fn = open('./language-data/synonyms-vn.txt', 'r', encoding='utf8')
synonyms_data = fn.read()
list_syn = ast.literal_eval(synonyms_data)

fn = open('./language-data/intents-vn.txt', 'r', encoding='utf8')
intents_data = fn.read()
intent_names = intents_data.split('\n')

keywords = {}
keywords_dict = {}

for intent in intent_names:
    keywords[intent] = []
    for synonym in list_syn[intent]:
        keywords[intent].append('.*\\b' + synonym + '\\b.*')

for key, value in keywords.items():
    keywords_dict[key] = re.compile('|'.join(value))


fn = open('./language-data/responses-vn.txt', 'r', encoding='utf8')
responses_data = fn.read()
responses = ast.literal_eval(responses_data)
