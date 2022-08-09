import re
import ast

intents = ''
intent_list = dict()
intent_files = ['./language-data/intents/intents-basic.txt',
                './language-data/intents/intents-categories.txt',
                './language-data/intents/intents-products.txt']
for intent_file in intent_files:
    fn = open(intent_file, 'r', encoding='utf8')
    intents += fn.read() + '\n'
intents_data = intents.split('\n')
del intents_data[-1]
for intent in intents_data:
    if intent == '':
        continue
    intent = intent.split('.')
    if(intent[0] not in intent_list):
        if(len(intent) > 1):
            intent_list[intent[0]] = {}
        else:
            intent_list.setdefault(intent[0])
    if(len(intent) > 1):
        intent_list[intent[0]][intent[1]] = []

synonym_list = dict()
synonym_keywords = dict()
synonym_files = ['./language-data/synonyms/synonyms-basic.txt',
                 './language-data/synonyms/synonyms-categories.txt',
                 './language-data/synonyms/synonyms-products.txt']
for synonym_file in synonym_files:
    fn = open(synonym_file, 'r', encoding='utf8')
    synonyms_data = ast.literal_eval(fn.read())
    synonym_list.update(synonyms_data)
for intent in intent_list:
    if(type(intent_list[intent]) is dict):
        for intent_b in synonym_list[intent]:
            synonym_keywords["{}.{}".format(intent, intent_b)] = []
            for synonym in synonym_list[intent][intent_b]:
                pattern = re.compile('.*\\b' + synonym + '\\b.*')
                synonym_keywords["{}.{}".format(
                    intent, intent_b)].append(pattern)
    else:
        synonym_keywords[intent] = []
        for synonym in synonym_list[intent]:
            pattern = re.compile('.*\\b' + synonym + '\\b.*')
            synonym_keywords[intent].append(pattern)

responses_keywords = dict()
response_files = ['./language-data/responses/responses-basic.txt',
                  './language-data/responses/responses-categories.txt',
                  './language-data/responses/responses-products.txt']
for response_file in response_files:
    fn = open(response_file, 'r', encoding='utf8')
    responses_data = ast.literal_eval(fn.read())
    responses_keywords.update(responses_data)
