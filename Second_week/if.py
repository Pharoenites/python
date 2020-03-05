age = input('Введите ваш возраст: ')
age = int(age)

def what_to_do_by_age(age):
    what_to_do = 'Возраст меньше 2 или больше 65'
    if 2 <= age <= 5:
        what_to_do = 'Пользователь должен учиться в детском саду'
    elif 6 <= age <= 16:
        what_to_do = 'Пользователь должен учиться в школе'
    elif 17 <= age <= 23:
        what_to_do = 'Пользователь должен учиться в университете'
    elif 24 <= age <= 65:
        what_to_do = 'Пользователь должен работать'
    return what_to_do

print(what_to_do_by_age(age))

