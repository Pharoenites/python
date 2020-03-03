dictionary = {
    "city": "Москва", 
    "temperature": "20"
}
print(dictionary['city'])

#1 способ
dictionary['temperature'] = str(int(dictionary['temperature']) - 5)
print(dictionary['temperature'])

#2 способ
temp = int(dictionary['temperature'])
temp = temp - 5
dictionary['temperature'] = str(temp)
print(dictionary['temperature'])


print(dictionary.get('country', "Россия"))
dictionary['date'] = "27.05.2019"
print(len(dictionary))

