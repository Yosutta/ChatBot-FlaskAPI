from lib.mysql_conn import mysqldb, mysqlerror

mysqlcursor = mysqldb.cursor()

query = ''' SELECT ahr00_virtuemart_products.virtuemart_product_id, product_name, category_name, ahr00_virtuemart_products_en_gb.metadesc, ahr00_virtuemart_products_en_gb.slug, product_price, currency_symbol, product_in_stock, ahr00_virtuemart_categories_en_gb.slug
            FROM ahr00_virtuemart_products
            INNER JOIN ahr00_virtuemart_products_en_gb
            ON ahr00_virtuemart_products.virtuemart_product_id = ahr00_virtuemart_products_en_gb.virtuemart_product_id
            INNER JOIN ahr00_virtuemart_product_prices
            ON ahr00_virtuemart_products.virtuemart_product_id = ahr00_virtuemart_product_prices.virtuemart_product_id
            INNER JOIN ahr00_virtuemart_currencies
            ON ahr00_virtuemart_product_prices.product_currency = ahr00_virtuemart_currencies.virtuemart_currency_id
            INNER JOIN ahr00_virtuemart_product_categories
            ON ahr00_virtuemart_products.virtuemart_product_id = ahr00_virtuemart_product_categories.virtuemart_product_id
            INNER JOIN ahr00_virtuemart_categories_en_gb
            ON ahr00_virtuemart_product_categories.virtuemart_category_id = ahr00_virtuemart_categories_en_gb.virtuemart_category_id
            WHERE ahr00_virtuemart_products.created_on IS NOT NULL
            '''
# value = (conversation_id, formatted_time)
mysqlcursor.execute(query)
data = mysqlcursor.fetchall()

files = ['./language-data/intents/intents-products.txt',
         './language-data/intents/intents-categories.txt',
         './language-data/intents/intents-categories.txt',
         './language-data/responses/responses-categories.txt',
         './language-data/responses/responses-products.txt',
         './language-data/synonyms/synonyms-products.txt',
         './products-data/products_price.txt',
         './products-data/products_inventory.txt',
         './products-data/products_link.txt']

for file in files:
    f = open(file, 'w')
    f.truncate(0)

categories = []
categories_slugs = []
products_price = dict()
products_inventory = dict()
products_link = dict()
responses_products = dict()
synonyms_products = dict()

# mysqldb.commit()
for row in data:
    # Create intents/intents-products.txt
    intent_name = 'sản phẩm.{}\n'.format(row[1].lower())
    f = open('./language-data/intents/intents-products.txt',
             "a", encoding="utf-8")
    f.write(intent_name)
    f.close()

    # Get list of products responses
    product_ans = 'Đây là đường dẫn đến sản phầm \n <a href="http://thinh01165.xyz/index.php/product/{}/{}-detail">{}</a> '.format(
        row[8], row[4], row[1])
    responses_products[intent_name.replace('\n', '')] = product_ans

    # Get list of meta data
    metadescs = row[3].split(' ')
    descs = set()
    for metadesc in metadescs:
        metadesc = metadesc.replace('-', ' ')
        descs.add(metadesc)
    synonyms_products[row[1].lower()] = descs

    # Get list of categories and categories_slug
    if row[2] not in categories:
        categories.append(row[2])

    if row[8] not in categories_slugs:
        categories_slugs.append(row[8])

    # Get list of products and its price
    products_price[intent_name.replace(
        '\n', '')] = '{}{}'.format(int(row[5]), row[6])

    # Get list of products and its inventory
    products_inventory[intent_name.replace(
        '\n', '')] = '{}'.format(row[7])

    # Get list of products and its link
    product_link = '<a href="http://thinh01165.xyz/index.php/product/{}/{}-detail">{}</a>'.format(
        row[8], row[4], row[1])
    products_link[intent_name.replace(
        '\n', '')] = product_link

# Create intents/categories.txt
responses_categories = dict()
categories_link = 'Đây danh sách các danh mục sản phẩm của chúng tôi \n'
for index in range(len(categories)):
    f = open('./language-data/intents/intents-categories.txt',
             "a", encoding="utf-8")
    category_name = 'danh mục.{}\n'.format(categories[index].lower())
    f.write(category_name)
    f.close()
    # Get responses categories data
    category_link = '<a href="http://thinh01165.xyz/index.php/product/{}">{}</a>'.format(
        categories_slugs[index], categories[index])
    category_ans = 'Đây là đường dẫn đến danh mục các sản phầm liên quan về \n {}'.format(
        category_link)
    responses_categories[category_name.replace('\n', '')] = category_ans

    categories_link += '{}. '.format(
        index + 1) + category_link + '\n'
    responses_categories['phân loại danh mục'] = categories_link

# Create categories-responses.txt
f = open('./language-data/responses/responses-categories.txt',
         "a", encoding="utf-8")
f.write(str(responses_categories))
f.close()

# Create products-responses.txt
f = open('./language-data/responses/responses-products.txt',
         "a", encoding="utf-8")
f.write(str(responses_products))
f.close()

# Create synonyms-products.txt
synonyms_data = {}
synonyms_data['sản phẩm'] = synonyms_products
f = open('./language-data/synonyms/synonyms-products.txt',
         "a", encoding="utf-8")
f.write(str(synonyms_data))
f.close()

# Create products-data/products_price.txt
f = open('./products-data/products_price.txt',
         "a", encoding="utf-8")
f.write(str(products_price))
f.close()

# Create products-data/products_inventory.txt
f = open('./products-data/products_inventory.txt',
         "a", encoding="utf-8")
f.write(str(products_inventory))
f.close()

# Create products-data/products_link.txt
f = open('./products-data/products_link.txt',
         "a", encoding="utf-8")
f.write(str(products_link))
f.close()

# Remove last blank line from each file
for file in files:
    with open(file, encoding="utf-8") as f_input:
        data = f_input.read().rstrip('\n')
    with open(file, 'w', encoding="utf-8") as f_output:
        f_output.write(data)
