my_dict = {'Vova':2002, 'Oleg': 2000, 'Nastya':2003, 'Pavel': 1999}

print(my_dict)
print(my_dict.get('Oleg'))
print(my_dict.get('Alexandr', 'Такого ключа нет'))

my_dict.update({'Ira': 2006,
                'Vlad':1998})
deleted_val = my_dict.pop('Nastya')
print('Удаленное значение:', deleted_val)
print(my_dict)


my_set = {1, 2, 3, 2, 2, 3, 1, 'Stas', 'Eva', 'Stas', True}
print('\nМножество: ', my_set)
my_set.add('Dima')
my_set.add(36)
my_set.remove('Eva')
print(my_set)
