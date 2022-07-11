import re
import ast
import pprint

intent_files = ['./language-data/intents/intents-basic.txt',
                './language-data/intents/intents-categories.txt',
                './language-data/intents/intents-products.txt']

intents = ''
for intent_file in intent_files:
    fn = open(intent_file, 'r', encoding='utf8')
    intents += fn.read()
intents_data = intents.split('\n')

# fn = open('./language-data/intents-vn.txt', 'r', encoding='utf8')
# intents_data = fn.read()
# intents_data = intents_data.split('\n')
# fn.close()

intent_list = {}

for intent in intents_data:
    intent = intent.split('.')
    if(intent[0] not in intent_list):
        if(len(intent) > 1):
            intent_list[intent[0]] = {}
        else:
            intent_list.setdefault(intent[0])
    if(len(intent) > 1):
        # intent_list[intent[0]].append(intent[1])
        intent_list[intent[0]][intent[1]] = []


synonym_files = ['./language-data/synonyms/synonyms-basic.txt',
                 './language-data/synonyms/synonyms-categories.txt',
                 './language-data/synonyms/synonyms-products.txt']

list_syn = dict()
for synonym_file in synonym_files:
    fn = open(synonym_file, 'r', encoding='utf8')
    synonyms_data = ast.literal_eval(fn.read())
    print(synonyms_data)
    list_syn.update(synonyms_data)

# fn = open('./language-data/synonyms-vn.txt', 'r', encoding='utf8')
# synonyms_data = fn.read()
# list_syn = ast.literal_eval(synonyms_data)
# fn.close()

print("List syn " + str(list_syn))


keywords = {}
keywords_dict = {}

# for intent in intent_list:
#     if(type(intent_list[intent]) is dict):
#         for intent_b in list_syn[intent]:
#             for synonym in list_syn[intent][intent_b]:
#                 intent_list[intent][intent_b].append(
#                     '.*\\b' + synonym + '\\b.*')
#     else:
#         for synonym in list_syn[intent]:
#             intent_list[intent].append('.*\\b' + synonym + '\\b.*')

for intent in intent_list:
    print(intent)
    if(type(intent_list[intent]) is dict):
        for intent_b in list_syn[intent]:
            keywords["{}.{}".format(intent, intent_b)] = []
            for synonym in list_syn[intent][intent_b]:
                pattern = re.compile('.*\\b' + synonym + '\\b.*')
                # pattern = ".*\\b' + synonym + '\\b.*"
                # pattern = re.compile("\b' + synonym + '\b")
                # pattern = re.compile(synonym)
                keywords["{}.{}".format(intent, intent_b)].append(pattern)
    else:
        keywords[intent] = []
        for synonym in list_syn[intent]:
            pattern = re.compile('.*\\b' + synonym + '\\b.*')
            # pattern = re.compile("\b' + synonym + '\b")
            # pattern = re.compile(synonym)
            keywords[intent].append(pattern)

# for key, value in keywords.items():
#     keywords_dict[key] = re.compile('|'.join(value))

print(keywords)

response_files = ['./language-data/responses/responses-basic.txt',
                  './language-data/responses/responses-categories.txt',
                  './language-data/responses/responses-products.txt']

responses = dict()
for response_file in response_files:
    fn = open(response_file, 'r', encoding='utf8')
    responses_data = ast.literal_eval(fn.read())
    responses.update(responses_data)

print("Responsés " + str(responses))

# fn = open('./language-data/responses-vn.txt', 'r', encoding='utf8')
# responses_data = fn.read()
# responses = ast.literal_eval(responses_data)
# fn.close()

print("Accessing data")


# Xin chào tạm biệt, món lều này có giá là bao nhiêu thế?
# Món lều này có giá là bao nhiêu thế?
# Món lều, bàn này có giá là bao nhiêu thế?

# Lều - Tên, Số người
# Thuyển - Loại
# Phụ kiện -
# Bàn Ghế
# Đèn - Cách sử dụng
# Camera Hành Trình - Số hiệu

# Dictionary sort
