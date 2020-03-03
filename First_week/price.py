def format_price(price):
    price = int(price)
    return f'Цена: {price} руб.'

call_function = format_price(56.24)
print(format_price(56.24))
print(call_function)