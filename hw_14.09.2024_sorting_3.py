# СОРТИРОВКА И ПОИСК. Часть 3.

# =============== Общие исходные 4 списка для всех задач ==============================

list_1 = [1, 89, 78, 0]
list_2 = [-50, -1000, 0]
list_3 = [11, -6, 13]
list_4 = [55, -99, 0, 33]

# =================================================================================


# Задача 1. Есть четыре списка целых. Необходимо их объединить в пятом списке. Полученный результат в зависимости от
# выбора пользователя отсортировать по убыванию или возрастанию. Найти значение, введенное пользователем,
# с использованием линейного поиска.

# list_merge = list_1 + list_2 + list_3 + list_4  # объединённый список
#
#
# def bubble_fun(some_list, direction):  # функция сортировки пузырьком
#     if direction.strip() == 'в' or direction.strip() == 'у':
#         res_list = some_list.copy()
#         flag = True
#         while flag:
#             flag = False
#             for i in range(len(res_list) - 1):
#                 if res_list[i] > res_list[i + 1]:
#                     flag = True
#                     res_list[i], res_list[i + 1] = res_list[i + 1], res_list[i]
#         return res_list if direction.strip() == 'в' else res_list[::-1]
#
#
# def linear_fun(some_list, num):  # функция линейного поиска индексов элементов в переданном списке
#     if num in some_list:
#         res_list = list()
#         for i, val in enumerate(some_list):
#             if val == num:
#                 res_list.append(str(i))
#         res_string = ', '.join(res_list)
#         print('Индекс загаданного числа в исходном списке: {}.'.format(res_string))
#     else:
#         print('Загаданного числа в исходном списке НЕТ! Одень очки и смотри в четыре!')
#
#
# print('Объединённый (исходный) список таков: {}'.format(list_merge))  # выводим объединённый список
#
# print('Как отсортировать список: в - по возрастанию, у - по убыванию')
# how_to_sort = input()
#
# print(bubble_fun(list_merge, how_to_sort))  # сортируем по запросу пользователя (в - по возрастанию, у - по убыванию)
#
# print('Загадайте число из объединённого (несортированного) списка:')
# num_of_list_merge = int(input())
#
# linear_fun(list_merge, num_of_list_merge)  # линейный поиск индексов загаданного элемента в исходном списке


# Задача 2. Есть четыре списка целых. Необходимо объединить в пятом списке только те элементы, которые уникальны
# для каждого списка. Полученный результат в зависимости от выбора пользователя отсортировать по убыванию или
# возрастанию. Найти значение, введенное пользователем, с использованием бинарного поиска.

# list_merge = list_1 + list_2 + list_3 + list_4  # объединяем списки
# list_merge_set = list(set(list_merge))  # список уникальных элементов
#
#
# def bubble_fun(some_list, direction):  # функция сортировки пузырьком
#     if direction.strip() == 'в' or direction.strip() == 'у':
#         res_list = some_list.copy()
#         flag = True
#         while flag:
#             flag = False
#             for i in range(len(res_list) - 1):
#                 if res_list[i] > res_list[i + 1]:
#                     flag = True
#                     res_list[i], res_list[i + 1] = res_list[i + 1], res_list[i]
#         return res_list if direction.strip() == 'в' else res_list[::-1]
#
#
# def binary_search(num_list, item):  # бинарный поиск индекса числа
#     bin_list = num_list.copy()
#     bin_list.sort()
#     low = 0
#     high = len(bin_list) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         guess = bin_list[mid]
#         if guess == item:
#             return mid, bin_list[mid]
#         if guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None
#
#
# print('Список уникальных элементов: {}'.format(list_merge_set))
#
# print('Как отсортировать список: в - по возрастанию, у - по убыванию')
# how_to_sort = input()
#
# print(bubble_fun(list_merge_set, how_to_sort))  # сортируем по запросу (в - по возрастанию, у - по убыванию)
#
# print('Загадайте число из списка уникальных элементов:')
# num_of_list_merge_set = int(input())
#
# index, value = binary_search(list_merge_set, num_of_list_merge_set)
#
# print('Индекс загаданного числа в сортированном по возрастанию списке: {}'.format(index))
# print('Загаданное число: {}'.format(value))
