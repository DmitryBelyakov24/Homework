# Практическое задание по теме: "Словари и множества"
print('Цель: Написать программу на языке Python, используя Pycharm, для работы со словарями и множествами.')

# Работа со славарями
my_dict = {'Demis': 1980, 'Felix': 1978, 'Mari': 1995}
print(my_dict)
print(my_dict['Felix'])
print(my_dict.get("Max"))
my_dict ['Dima'] = 1984
print(my_dict)
my_dict.update({'Mustafa': 1989, 'Nikolay': 1982})
print(my_dict)
del my_dict['Mustafa']
print(my_dict)

# Множества
my_set = {'Urban', 2024, 'September', 54.12, 5, 5, 2024, 'Urban', 54.12}
print(my_set)
my_set.update({'Student', (1, 345, 789)})
print(my_set)
print(my_set.remove(54.12))
print(my_set)
print(my_set.discard('September'))
print(my_set)

