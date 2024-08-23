def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params()
print_params(3)
print_params(4, 5)
print_params(b='25')
print_params(c=[1, 2, 3])

values_list_2 = [54.32, 'Строка']
values_list = [75, 'D', 4]
print_params(*values_list)
values_dict = {'a': 67, 'b': 'D', 'c': 9}
print_params(**values_dict)
print_params(*values_list_2, 42)
