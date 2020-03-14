#def ask_user():
#    answer = ''
#    while answer != 'Хорошо':
#        print('Как дела?')
#        answer = input()

dict = {
    "1": "Привет!", 
    "2": "Хорошо",
    "3": "Программирую", 
    "4": "Пока"
}

def ask_user():
    while True:
        try:
            question = input()
            print(dict[question])
        except KeyboardInterrupt:
            print('Пока!')
            break


ask_user()