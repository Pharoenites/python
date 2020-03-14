balance = -10
print(bool(balance < 0))
if balance < 0:
    print('Пожалуйста, пополните баланс!')

balance = 100
price = 200
print(bool(balance < 0 or price > balance))
if balance < 0 or price > balance:
    print('Пожалуйста, пополните баланс!')

balance = 1000
price = 200
    
if balance > price:
    print('Спасибо за покупку')
else:
    print('Пожалуйста, пополните баланс!')

def weather(temperature):
    if temperature < 0:
        return 'На улице холодно!'
    elif 0 <= temperature <= 15:
        return 'На улице прохладно'
    elif 15 <= temperature <= 25:
        return 'На улице тепло'
    else:
        return 'На улице жарко'

print(weather(20))









