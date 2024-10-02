# Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"
print('Цель: закрепить навык решения задач при помощи цикла for, применив знания об основных типах данных')

# Задача "Всё не так уж просто":
# Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Используя этот список составьте второй список primes содержащий только простые числа.
# А так же третий список not_primes, содержащий все не простые числа.
# Выведите списки primes и not_primes на экран(в консоль).

# Первый вариант
print('##################################################################')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    if numbers[i] < 2:
        continue
    else:
        is_prime = True
        for j in range(2, int((numbers[i] ** 1/2) + 1)):
            if numbers[i] % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(numbers[i])
        else:
            not_primes.append(numbers[i])
print('Primes', primes)
print('Not Primes', not_primes)

# Второй вариант
print('##################################################################')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
k = 0
while k < len(numbers):
    # w = numbers[k]
    if numbers[k] < 2:
        #not_primes.append(numbers[k])
        pass
    else:
        is_prime = True
        g = int((numbers[k] ** 1 / 2) + 1)
        for y in range(2, g):
            if numbers[k] % y == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(numbers[k])
        else:
            not_primes.append(numbers[k])
    k += 1
print('Primes', primes)
print('Not Primes', not_primes)
