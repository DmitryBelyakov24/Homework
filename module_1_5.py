# Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи
print('Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"')

#  Задайте переменные разных типов данных:
immutable_var = "Student", 5.56, 'Ландыш', 1716
print(immutable_var)

#  Изменение значений переменных:
# immutable_var[0] = "Urban"
# print(immutable_var) - невозможно изменить значения , т.к. в кортеже значение (список ) постоянны и не меняются.
# А вот в строке Можно!!

# Создание изменяемых структур данных:
mutable_list = ["Moto", "Auto", 2420, 'Ninja']
print(mutable_list)
mutable_list.extend(['Ландыш', 5.56, "Student"])
print(mutable_list)
mutable_list.remove(2420)
print(mutable_list)
mutable_list[3] = 2024
print(mutable_list)