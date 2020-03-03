def get_summ(one, two, delimiter = '&'):
    one = str(one)
    two = str(two)
    return f'{one}{delimiter}{two}'

call_function = get_summ("Learn", "python")
print(call_function)
call_function = call_function.upper()
print(call_function)