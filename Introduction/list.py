phones = ['IPhone', 'Samsung', 'Xaiomi']
print(phones)
phones.append('Honor')
print(phones)
print(len(phones))
print(phones.count('F'))
print(phones.count('Xaiomi'))
print(phones[3])
print(phones[1:3])
print(phones[:2])
print(phones[-1]) #первый с конца
print(phones.index('Samsung'))

test_list = ['a', 'z', 'b']
test_list.sort()
print(test_list)
print('z' in test_list)
print('zzz' in test_list)


test = ['a', 'z', 'b', 'a']
print(test)
del test[2]
print(test)
test.remove('a')
print(test)