import ast

fn = open('./products-data/products_price.txt', 'r', encoding='utf8')
products_price = fn.read()
products_price = ast.literal_eval(products_price)
fn.close()

fn = open('./products-data/products_inventory.txt', 'r', encoding='utf8')
products_inventory = fn.read()
products_inventory = ast.literal_eval(products_inventory)
fn.close()

fn = open('./products-data/products_link.txt', 'r', encoding='utf8')
products_link = fn.read()
products_link = ast.literal_eval(products_link)
fn.close()
