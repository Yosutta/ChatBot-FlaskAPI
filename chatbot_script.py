import re

from process_data import responses, keywords
from products_data import products_price, products_inventory, products_link


def getProductPrice(product_name):
    return products_price[product_name]


def getProductInventory(product_name):
    return products_inventory[product_name]


def getProductLink(product_name):
    return products_link[product_name]


def getProductsIntent(intents):
    filtered_dict = {k: v for (k, v) in intents.items() if 'sản phẩm' in k}
    if(len(filtered_dict) == 0):
        return None
    else:
        products_intent = list(filtered_dict.keys())
        return products_intent


def getCategoriesIntent(intents):
    filtered_dict = {k: v for (k, v) in intents.items() if 'danh mục' in k}
    if(len(filtered_dict) == 0):
        return None
    else:
        categories_intent = list(filtered_dict.keys())
        return categories_intent


def prepareCategoriesIntentAnswer(categories_intent=[]):
    category = categories_intent[0].split('.')[1].capitalize()
    answer = 'Bạn hãy cung cấp thêm thông tin về tên sản phẩm trong danh mục {} nhé!'.format(
        category)
    return createDict("answer", answer)


def prepareProductPriceAnswer(product_intent):
    product_price = getProductPrice(product_intent)
    product_link = getProductLink(product_intent)
    return 'Giá của sản phẩm {} là {}.'.format(product_link, product_price)


def prepareProductInventoryAnswer(product_intent):
    product_inventory = getProductInventory(product_intent)
    product_link = getProductLink(product_intent)
    return 'Số tồn kho của sản phẩm {} là {}.'.format(product_link, product_inventory)


def createDict(key, value):
    newDict = {}
    newDict[key] = value
    return newDict


def getAnswerDirection(intents):
    # Sửa lại code lấy Intent cao nhất
    try:
        # Lấy ra tên ngữ cảnh có điểm số cao nhất
        highest_intent = max(intents, key=intents.get)
        # Lấy điểm số của ngữ cảnh đạt điểm cao nhất
        highest_intent_value = intents[highest_intent]
        # Lấy ra các ngữ cảnh có cùng điểm cao nhất
        filtered_dict = {k: v for (k, v) in intents.items()
                         if highest_intent_value == v}

        main_intent = None
        # Nếu danh sách chỉ có một ngữ cảnh có điểm cao nhất lấy ngữ cảnh đó
        if(len(filtered_dict) == 1):
            main_intent = list(filtered_dict.keys())[0]
        # Nếu danh sách có hơn 2 lấy ngữ cảnh theo sắp xếp thứ tự cuối cùng
        else:
            main_intent = list(filtered_dict.keys())[-1]

        main_intents = main_intent.split('.')

        match main_intents[0]:
            case 'danh mục':
                # Đưa link danh mục sản phẩm cho khách hàng
                return createDict("key", main_intent)
                # prepareCategoriesListAnswer()
            case 'sản phẩm':
                return createDict("key", main_intent)
            case 'câu hỏi':
                products_intent = getProductsIntent(intents)
                match main_intents[1]:
                    case 'giá tiền':
                        # Nếu không tồn tại tên sản phẩm trong câu hỏi
                        if not products_intent:
                            categories_intent = getCategoriesIntent(intents)
                            if len(categories_intent) > 0:
                                return prepareCategoriesIntentAnswer(categories_intent)
                            else:
                                return createDict("key", main_intent)
                        # Ngược lại nếu tồn tại tên sản phẩm trong câu hỏi
                        else:
                            price_answer = ''
                            for product_intent in products_intent:
                                intent_answer = prepareProductPriceAnswer(
                                    product_intent)
                                price_answer += intent_answer + '\n'
                            return createDict("answer", price_answer)
                    case 'số tồn kho':
                        if not products_intent:
                            categories_intent = getCategoriesIntent(intents)
                            if len(categories_intent) > 0:
                                return prepareCategoriesIntentAnswer(categories_intent)
                            else:
                                return createDict("key", main_intent)
                        else:
                            inventory_answer = ''
                            for product_intent in products_intent:
                                intent_answer = prepareProductInventoryAnswer(
                                    product_intent)
                                inventory_answer += intent_answer + '\n'
                            return createDict("answer", inventory_answer)

            case default:
                return createDict("key", main_intent)

    except:
        return createDict("key", "không rõ")


def createAnswer(message):
    user_input = message.lower()

    matched_intent = {}

    for intent in keywords:
        intent_arr = intent.split(".")
        weight = 1
        match intent_arr[0]:
            case 'câu hỏi':
                weight = 3
            case 'default':
                weight = 1
        for pattern in keywords[intent]:
            if(re.search(pattern, user_input)):
                if intent not in matched_intent:
                    matched_intent[intent] = weight
                elif intent in matched_intent:
                    matched_intent[intent] += weight

    key = ''
    if len(matched_intent) == 0:
        key = 'không rõ'
    elif len(matched_intent) == 1:
        key = list(matched_intent.keys())[0]
    elif len(matched_intent) > 1:
        intentSum = sum(matched_intent.values())
        for intent in matched_intent:
            matched_intent[intent] = matched_intent[intent] / intentSum
        del intentSum
        answer_direction = getAnswerDirection(matched_intent)

        match list(answer_direction.keys())[0]:
            case "answer":
                return answer_direction["answer"]
            case "key":
                key = answer_direction["key"]

    else:
        key = 'không rõ'

    return responses[key]


# if câu hỏi:
# 	Check sản phẩm
# 	If no sản phẩm
# 		Check danh mục
# 		if Danh mục
# 			Hỏi sản phẩm danh mục muốn kiểm tra
# 		Else
# 			Yêu cầu khách hàng cung cấp thôn tin sản phẩm
# 	Else
# 		Đưa câu trả lời câu hỏi

# elif danh mục:
#   If danh mục[1] ==0
#       Liệt kê các danh mục
#   Else
#       Đưa link danh mục[1]
# elif sản phẩm:
# 	Đưa link sản phẩm
# elif:
