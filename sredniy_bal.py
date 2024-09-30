# Дополнительное практическое задание по модулю*
print('Дополнительное практическое задание по модулю: "Базовые структуры данных."')

#Задание "Средний балл":
#Вам необходимо решить задачу из реальной жизни:
#"школьные учителя устали подсчитывать вручную " \
#"средний балл каждого ученика, поэтому вам предстоит автоматизировать этот процесс":
#На вход даны следующие данные:
#Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
#Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
#Например: 'Aaron' - [5, 3, 3, 5, 4]
#Множество students содержит неупорядоченную последовательность имён всех учеников в классе.
#Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика,
#а значением - его средний балл.


grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

new_dictionary = {}  # Создаем пустой словарь
name = list(students)  # приобразуем множеству в класс List - создаем список studentes
print(type(name))  # проверяеv преобразования
name.sort()  # применяем метод sort (он применяется к спискам)

# заполняем словарь используем метод update

# Первый вариант:
new_dictionary.update({name[0]: sum(grades[0]) / len(grades[0]), name[1]: sum(grades[1]) / len(grades[1]),
                       name[2]: sum(grades[2]) / len(grades[2]), name[3]: sum(grades[3]) / len(grades[3]),
                       name[4]: sum(grades[4]) / len(grades[4])})
print(new_dictionary)

# второй вариант:
new_dictionary_ = dict()
new_dictionary_.update({name[0]: sum(grades[0]) / len(grades[0])})
new_dictionary_.update({name[1]: sum(grades[1]) / len(grades[1])})
new_dictionary_.update({name[2]: sum(grades[2]) / len(grades[2])})
new_dictionary_.update({name[3]: sum(grades[3]) / len(grades[3])})
new_dictionary_.update({name[4]: sum(grades[4]) / len(grades[4])})
print(new_dictionary_)

# PS. Как на практике будет ПРАВИЛЬНЕЕ ( везде верно)?????????
