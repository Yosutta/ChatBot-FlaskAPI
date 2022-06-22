import re

from processed_data import responses, keywords_dict


def createAnswer(message):
    user_input = message.lower()

    if user_input in ['thoat', 'quit']:
        return ('Tạm biệt và hẹn gặp lại nhé!')

    matched_intent = None

    for intent, pattern in keywords_dict.items():
        if re.search(pattern, user_input):
            matched_intent = intent

    key = 'không rõ'

    if matched_intent in responses:
        key = matched_intent

    return responses[key]


# while(True):

#     user_input = input(">").lower()

#     if user_input in ['thoat', 'quit']:
#         print('Tạm biệt và hẹn gặp lại nhé!')
#         break

#     matched_intent = None

#     for intent, pattern in keywords_dict.items():
#         if re.search(pattern, user_input):
#             matched_intent = intent

#     key = 'không rõ'

#     if matched_intent in responses:
#         key = matched_intent

#     print(responses[key])
