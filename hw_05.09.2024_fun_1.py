# ФУНКЦИИ. ЧАСТЬ 1

from time import sleep

# Задание 1. Напишите функцию, которая отображает на экран форматированный текст, указанный ниже:
# “Don't compare yourself with anyone in this world…
# if you do so, you are insulting yourself.”
#                                         Bill Gates

# some_text = '''
#     “Don't compare yourself with anyone in this world…
#      if you do so, you are insulting yourself.”
#                                             Bill Gates
# '''
#
# def print_text(text):
#     print(text)
#
#
# print(some_text)


# Задание 2. Напишите функцию, которая принимает два числа в качестве параметра и отображает все четные числа
# между ними.

# num_1 = -30
# num_2 = -11
#
#
# def print_of_even_between(x, y):
#     num_list = [num for num in range(min(x, y) + 1, max(x, y)) if num % 2 == 0]
#     print(num_list)
#
#
# print_of_even_between(num_1, num_2)


# Задание 3. Напишите функцию, которая отображает пустой или заполненный квадрат из некоторого символа. Функция
# принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа:
# ■ если она равна True, квадрат заполненный;
# ■ если False, квадрат пустой.

# l = 13
# s = 'u'
# b = False
#
#
# def print_square(l, s, b):
#     if b:
#         for i in range(l):
#             sleep(0.5)
#             print(((s + '  ') * l).ljust(l))
#     else:
#         for i in range(l):
#             if 0 < i < (l - 1):
#                 sleep(0.5)
#                 print(s, ''.center(l * 3 - 6), s)
#             else:
#                 sleep(0.5)
#                 print((s + '  ') * l)
#
#
# print_square(l, s, b)


# Задание 4. Напишите функцию, которая возвращает минимальное из пяти чисел. Числа передаются в качестве параметров.

# a, b, c, d, e = 458, -7, 0, -98, 25
#
#
# def min_of_nums(*args):
#     return min(args)
#
#
# print(min_of_nums(a, b, c, d, e))


# Задание 5. Напишите ф-ю, которая возвращает произведение чисел в указанном диапазоне. Границы диапазона
# передаются в качестве параметров. Если границы диапазона перепутаны (например, 5-верхняя граница, 25-нижняя),
# их нужно поменять местами.

# lim_1 = 6
# lim_2 = 1
#
#
# def mul_func(x, y):
#     res = 1
#     for num in range(min(x, y), max(x, y) + 1):
#         res *= num
#     return res
#
#
# print(mul_func(lim_1, lim_2))


# Задание 6. Напишите функцию, которая считает количество цифр в числе. Число передаётся в качестве параметра.
# Из функции нужно вернуть полученное количество цифр. Например, если передали 3456, количество цифр будет 4.

# some_num = -6912
#
#
# def num_of_digits(num):
#     count = 0
#     while True:
#         num /= 10
#         count += 1
#         if abs(num) < 1:
#             break
#     return count
#
#
# print(num_of_digits(some_num))


# Задание 7. Напишите функцию, которая проверяет, является ли число палиндромом. Число передаётся в качестве
# параметра. Если число палиндром нужно вернуть из функции true, иначе false.
# «Палиндром» — это число, у которого первая часть цифр равна второй перевернутой части цифр. Например,
# 123321—палиндром (первая часть 123, вторая 321, которая после переворота становится 123), 546645—палиндром,
# а 421987 — не палиндром.

# some_number = 546645
#
#
# def check_pal(num):
#     check_res = True if list(str(num)) == list(str(num))[::-1] else False
#     return check_res
#
#
# print(check_pal(some_number))
