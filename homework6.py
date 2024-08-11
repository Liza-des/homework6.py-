my_dict = {'Maxim': 1970, 'Sergey': 1965, 'Misha': 1985}
print('Dict: ', my_dict)
print('Existing value: ', my_dict.get('Misha'))
print('Not existing value: ', my_dict.get('Lera'))
my_dict.update({'Lera':2000, 'Masha':1995})
print('Modified dictionary: ', my_dict)
a = my_dict.pop('Sergey')
print('Modified dictionary 2: ', my_dict)
print('Deleted value: ', a)

my_set = {15, 1, 3, 18, 'apples', 3, 18, 35, False}
print('Set: ', my_set)
my_set = {15, 1, 3, 18, 'apples', 3, True, 15, (1, 2, 3, 3, 4)}
print('Modified set: ', my_set)