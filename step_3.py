from step_1 import transform_products_to_list
from data import products_string
from pprint import pprint

def group_products_by_customer_and_invoice(products_string):
    products_list = transform_products_to_list(products_string)
    
    products = {}
    
    for product in products_list:
        customer_id = product[-2]
        invoice_id = product[0]
        
        products.setdefault(customer_id, {})
        products[customer_id].setdefault(invoice_id, [])
        products[customer_id][invoice_id].append(product)
        
    return products

products = group_products_by_customer_and_invoice(products_string)
pprint(products)
print('*******************************')
customer = products['12583']
# print(customer)
invoice = customer['536370']
# print(invoice)
row_item = invoice[1]
# print(row_item)
description = row_item[2]
print(description)

result = products['12583']['536370'][1][2]
print(result)