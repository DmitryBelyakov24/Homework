# Практическая работа по уроку "Динамическая типизация"
# Цель: Написать программу на языке Python, используя Pycharm, для демонстрации динамической типизации.

name = "Dmitry"

print("Name:", name) # Вывод перменной 'name' на экран
# print(type(name)) # Вывод на экран значенния типа переменной
# print(name, type(name)) # Вывод на экран переменной и значение типа переменной

age = 40

print("Age:", age)

# a = 15
# print (age + a)

age = age + 1
print("New Age:", age)

is_student = "Dmitry"

print("Is Student:", is_student == name )