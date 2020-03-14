a = input('Введите первую строку: ')
b = input('Введите вторую строку: ')

def compare_strings(a, b):
    if (type(a) == str and type(b) == str) == False:
        return 0
    if a == b:
        return 1
    if a != b and len(a) > len(b):
        return 2
    if a != b and b == 'learn':
        return 3
        
print(compare_strings(a, b))


