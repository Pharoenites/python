product = {
    "name": "IPhone",
    "stock": 24,
    "price": 444.5
}
print(product)
print(len(product))

product['memory'] = 10
print(product)

print(product['name'])
print(product.get('name'))
print(product.get('lol', 0))

del product['stock']
print(product)

phones = ['IPhone', 'Samsung', 'Xaiomi']
product['recommend'] = phones
print(product)
print(product['recommend'][1])