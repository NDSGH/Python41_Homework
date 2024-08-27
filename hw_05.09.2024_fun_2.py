# ФУНКЦИИ. ЧАСТЬ 2

from math import pow

# Задание 1. Напишите функцию, вычисляющую произведение элементов списка целых. Список передаётся в качестве
# параметра. Полученный результат возвращается из функции.

# list_of_int = [1, 2, 3, 4]
#
#
# def mul_of_elements(some_list):
#     res = 1
#     for i in range(len(some_list)):
#         res *= some_list[i]
#     return res
#
#
# print(mul_of_elements(list_of_int))


# Задание 2. Напишите функцию для нахождения минимума в списке целых. Список передаётся в качестве параметра.
# Полученный результат возвращается из функции.

# list_of_int_2 = [1, 2, 3, 4, -9]
#
#
# def search_of_min(some_list):
#     return min(some_list)
#
#
# print(search_of_min(list_of_int_2))


# Задание 3. Напишите функцию, определяющую количество простых чисел в списке целых. Список передаётся в качестве
# параметра. Полученный результат возвращается из функции.

# list_of_int_3 = [1, 2, 17, 3, 4, 9, 2]
#
#
# def search_of_prime(some_list):
#     prime_list = list()
#     divider = 0
#     for num in some_list:
#         for i in range(1, num + 1):
#             if num % i == 0:
#                 divider += 1
#         if divider <= 2 and num > 1:
#             prime_list.append(num)
#         divider = 0
#     return len(prime_list)
#
#
# print(search_of_prime(list_of_int_3))


# Задание 4. Напишите функцию, удаляющую из списка целых некоторое заданное число. Из функции нужно вернуть
# количество удаленных элементов.

# list_of_int_4 = [2, 1, 2, 17, 3, 2, 4, 9, 2, 2, 2]
# deleted_num = 2
#
#
# def eraser(some_list, set_num):
#     shallow_copy = list(some_list)
#     for num in shallow_copy:
#         if num == set_num:
#             some_list.remove(num)
#     return len(shallow_copy) - len(some_list)
#
#
# print(eraser(list_of_int_4, deleted_num))
#
# print(list_of_int_4)


# Задание 5. Напишите функцию, которая получает два списка в качестве параметра и возвращает список, содержащий
# элементы обоих списков.

# ext_list_1 = ['Слон', 'Мыло', 'Рубаха', 'Мамба']
# ext_list_2 = ['Пила', 77, 'Дрель', 88]
#
#
# def extender(list_1, list_2):
#     list_1.extend(list_2)
#     return list_1
#
#
# print(extender(ext_list_1, ext_list_2))


# Задание 6. Напишите функцию, высчитывающую степень каждого элемента списка целых. Значение для степени передаётся
# в качестве параметра, список тоже передаётся в качестве параметра. Функция возвращает новый список, содержащий
# полученные результаты.

# list_of_int_5 = [2, 1, 2, -3]
# set_pow = 5
#
#
# def list_pow(some_list, set_pow):
#     swallow_copy = list(some_list)
#     res_list = [pow(num, set_pow) for num in swallow_copy]
#     return res_list
#
#
# pow_list = list_pow(list_of_int_5, set_pow)
#
# print(list_of_int_5)
# print(pow_list)
