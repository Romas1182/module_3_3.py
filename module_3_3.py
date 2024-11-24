def print_params(a=1, b = 'строка', c = True):
    print(a, b, c)

print_params()                             # вызов без аргументов
print_params(6, 'str', False)
print_params(56, 'ns')               # вызов с разным количеством аргументов
print_params(c = 'ghj')
print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['str', 2, False]
values_dict = {'a': 8, 'b': 55, 'c': 77}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [9, 'str']
print_params(*values_list_2, 42)
