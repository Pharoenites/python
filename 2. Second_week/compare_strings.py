a = input('Введите первую строку: ')
b = input('Введите вторую строку: ')

def compare_strings(a, b):
    if (type(a) != str or type(b) != str):
        return 0
    elif a == b:
        return 1
    elif a != b and len(a) > len(b):
        return 2
    elif a != b and b == 'learn':
        return 3
    else:
        print('else')
        
print(compare_strings(a, b))
