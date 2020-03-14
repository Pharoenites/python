def cut_cake(people):
    try:
        z = 1 / people
        print(f'Каждый получит {z} пирога')
    except(ZeroDivisionError, TypeError):
        print("Не могу поделить")

cut_cake(0)
cut_cake('d')