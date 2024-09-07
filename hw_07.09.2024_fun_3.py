# ФУНКЦИИ. ЧАСТЬ 3

from random import sample

# Задание 1. Написать рекурсивную функцию нахождения наибольшего общего делителя двух целых чисел.

# num_1 = 6
# num_2 = 16
#
#
# def greatest_common_divisor(x, y):
#     if max(x, y) % min(x, y) == 0:
#         return min(x, y)
#     return greatest_common_divisor(min(x, y), max(x, y) % min(x, y))
#
#
# print(greatest_common_divisor(num_1, num_2))


# Задание 2. Написать игру «Быки и коровы». Программа «загадывает» четырёхзначное число и играющий должен
# угадать его. После ввода пользователем числа программа сообщает, сколько цифр числа угадано (быки) и сколько
# цифр угадано и стоит на нужном месте (коровы). После отгадывания числа на экран необходимо вывести количество
# сделанных пользователем попыток. В программе необходимо использовать рекурсию.

# num_list = list(range(10))  # подготовка ряда чисел для генерации загаданного слова
#
# secret_list = [str(num) for num in sample(num_list, 4)]  # собираем список случайных цифр в формате str (один раз)
#
# current_list = ['#'] * len(secret_list)
# print(' '.join(current_list))  # выводим скрытое загаданное число на экран
#
#
# def counter_bull(list1, list2):  # функция счёта быков
#     counter = 0
#     set_list = list(set(list2))
#     for i in range(len(set_list)):
#         if list1.count(set_list[i]) != 0:
#             counter += list1.count(set_list[i])
#     return counter
#
#
# def counter_cow(list1, list2):  # функция счёта коров
#     counter = 0
#     for i in range(len(list1)):
#         if list1[i] == list2[i]:
#             counter += 1
#     return counter
#
#
# def rec_fun():
#     input_number = input('Введите четырёхзначное число: ')
#
#     bull = counter_bull(secret_list, input_number)
#     cow = counter_cow(secret_list, input_number)
#
#     for i in range(len(secret_list)):
#         if secret_list[i] == input_number[i]:
#             current_list[i] = input_number[i]  # открываем угаданные цифры
#
#     print(f'Угаданное количество цифр: {bull} (БЫКИ)')
#     print(f'Угаданное количество цифр на своём месте: {cow} (КОРОВЫ)')
#     print(' '.join(current_list))
#
#     counter_rep = 1  # счётчик количества попыток угадать число
#
#     if current_list == list(input_number):
#         return counter_rep  # базовый случай
#     return counter_rep + rec_fun()  # рекурсивный случай
#
#
# print(f'Количество попыток: {rec_fun()}')


# Доп. задача. Напишите программу, кот. считывает натуральное число n и выводит первые n чисел
# последовательности Фибоначчи. На вход программе подаётся одно число n (n <= 100) - количество членов
# последовательности. Программа должна вывести члены последовательности Фибоначчи, отделённые символом пробела.

# n = 20  # задаём количество выводимых членов последовательности
#
#
# def fib_fun(int_num):
#     if int_num in (1, 2):
#         return 1
#     return fib_fun(int_num - 1) + fib_fun(int_num - 2)
#
#
# fib_list_gen = (str(fib_fun(num)) for num in range(1, n + 1) if n <= 100)  # создаём генератор чисел Фибоначчи
#
# fib_row = ' '.join(list(fib_list_gen))  # создаём список чисел и разделяем числа пробелами (по условию)
#
# print(fib_row)  # выводим результат


