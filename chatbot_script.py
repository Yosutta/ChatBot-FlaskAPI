import re

from process_data import responses_keywords, synonym_keywords
from products_data import products_price, products_inventory, products_link


def getProductPrice(product_name):
    return products_price[product_name]


def getProductInventory(product_name):
    return products_inventory[product_name]


def getProductLink(product_name):
    return products_link[product_name]


def createDict(key, value):
    newDict = {}
    newDict[key] = value
    return newDict


def prepareCategoriesIntentAnswer(categories_intent=[]):
    category = categories_intent[0].split('.')[1].capitalize()
    answer = 'Please provide information of the product in the {} category!'.format(
        category)
    return createDict("answer", answer)


def filterIntentsWithHighestValue(matched_intents):
    highest_intent_value = max(matched_intents.values())
    filtered_dict = {k: v for (k, v) in matched_intents.items()
                     if highest_intent_value == v}
    return filtered_dict


def getAllHighestValueIntents(highest_value_intents):
    main_intent = None
    if(len(highest_value_intents) == 1):
        main_intent = list(highest_value_intents.keys())[0]
    else:
        main_intent = list(highest_value_intents.keys())[-1]
    return main_intent


def getProductsFromMatchedIntents(intents):
    filtered_dict = {k: v for (k, v) in intents.items() if 'sản phẩm' in k}
    if(len(filtered_dict) == 0):
        return None
    else:
        products_intent = list(filtered_dict.keys())
        return products_intent


def getCategoriesFromMatchedIntent(intents):
    filtered_dict = {k: v for (k, v) in intents.items() if 'danh mục' in k}
    if(len(filtered_dict) == 0):
        return None
    else:
        categories_intent = list(filtered_dict.keys())
        return categories_intent


def returnAltAnswerForUnavailableProductIntent(matched_intents, main_intent):
    categories_intent = getCategoriesFromMatchedIntent(
        matched_intents)
    if len(categories_intent) > 0:
        return prepareCategoriesIntentAnswer(categories_intent)
    else:
        return createDict("key", main_intent)


def returnProductInventory(products_intent):
    inventory_answer = ''
    for product_intent in products_intent:
        product_inventory = getProductInventory(product_intent)
        product_link = getProductLink(product_intent)
        intent_answer = '{}"s inventory number is {}.'.format(
            product_link, product_inventory)
        inventory_answer += intent_answer + '\n'
    return createDict("answer", inventory_answer)


def returnProductPrice(products_intent):
    price_answer = ''
    for product_intent in products_intent:
        product_price = getProductPrice(product_intent)
        product_link = getProductLink(product_intent)
        intent_answer = '{} price is {}.'.format(
            product_link, product_price)
        price_answer += intent_answer + '\n'
    return createDict("answer", price_answer)


def MultipleRegconizedIntent(matched_intents):
    try:
        highest_value_intents = filterIntentsWithHighestValue(matched_intents)
        main_intent = getAllHighestValueIntents(
            highest_value_intents)
        splitted_main_intents = main_intent.split('.')

        match splitted_main_intents[0]:
            case 'câu hỏi':
                products_intent = getProductsFromMatchedIntents(
                    matched_intents)
                if not products_intent:
                    return returnAltAnswerForUnavailableProductIntent(matched_intents, main_intent)
                else:
                    match splitted_main_intents[1]:
                        case 'giá tiền':
                            return returnProductPrice(products_intent)
                        case 'số tồn kho':
                            return returnProductInventory(products_intent)
            case default:
                return createDict("key", main_intent)

    except:
        return createDict("key", "không rõ")

# Hàm trả về chuỗi không rõ


def noRecognizedIntent():
    return 'không rõ'


def SingleRecognizedIntent(matched_intents):
    return list(matched_intents.keys())[0]


def getMatchedIntents(user_input):
    matched_intents = dict()
    for keyword_index in synonym_keywords:
        intent_arr = keyword_index.split(".")
        weight = 1
        match intent_arr[0]:
            case 'câu hỏi':
                weight = 3
            case 'default':
                weight = 1
        for pattern in synonym_keywords[keyword_index]:
            if(re.search(pattern, user_input)):
                if keyword_index not in matched_intents:
                    matched_intents[keyword_index] = weight
                elif keyword_index in matched_intents:
                    matched_intents[keyword_index] += weight
    return matched_intents


def createAnswer(message):
    user_input = message.lower()

    matched_intents = getMatchedIntents(user_input)
    key = ''

    if len(matched_intents) == 0:
        key = noRecognizedIntent()
    elif len(matched_intents) == 1:
        key = SingleRecognizedIntent(matched_intents)
    elif len(matched_intents) > 1:
        answer_direction = MultipleRegconizedIntent(matched_intents)
        match list(answer_direction.keys())[0]:
            case "answer":
                return answer_direction["answer"]
            case "key":
                key = answer_direction["key"]
    else:
        key = 'không rõ'

    return responses_keywords[key]
