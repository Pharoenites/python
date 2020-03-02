#price = 100
#discount = 5
#price_with_discount = price - price * discount / 100
#print(price_with_discount)

def discounted(price, discount, max_discount=20):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)

product = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 10}

product['price_discounted'] = discounted(product['price'], product['discount'])

discounted(100, 50, max_discount = 100)



