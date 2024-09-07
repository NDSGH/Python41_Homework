# СОРТИРОВКА И ПОИСК. Часть 1.

import re

# Задача 1. Необходимо отсортировать первые две трети списка в порядке возрастания, если среднее арифметическое
# всех элементов больше нуля; иначе — лишь первую треть. Остальную часть списка не сортировать, а расположить
# в обратном порядке.

# list_1 = [12, -5, 79, 1022, -273, 2, 17, 458, 0]  # исходный список
#
#
# def avg(some_list):
#     if len(some_list) == 0:
#         raise ZeroDivisionError
#     return sum(some_list) / len(some_list)
#
#
# def bubble_fun(some_list):
#     slice_list = some_list[:2 * len(some_list) // 3] if avg(some_list) > 0 else some_list[:len(some_list) // 3]
#     flag = True
#     while flag:
#         flag = False
#         for i in range(len(slice_list) - 1):
#             if slice_list[i] > slice_list[i + 1]:
#                 flag = True
#                 slice_list[i], slice_list[i + 1] = slice_list[i + 1], slice_list[i]
#     return slice_list + some_list[len(slice_list):][::-1]
#
#
# try:
#     print('Исходный список: {}'.format(list_1))
#     print('Среднее арифметическое: {:.1f} {}'.format(avg(list_1), '> 0' if avg(list_1) > 0 else ''))
#     print('Отсортированный список: {}'.format(bubble_fun(list_1)))
# except BaseException:
#     print('Что-то пошло не так!')


# Задача 2. Написать программу «успеваемость». Пользователь вводит 10 оценок студента. Оценки от 1 до 12.
# Реализовать меню для пользователя:
# ■ Вывод оценок (вывод содержимого списка);
# ■ Пересдача экзамена (пользователь вводит номер элемента списка и новую оценку);
# ■ Выходит ли стипендия (стипендия выходит, если средний бал не ниже 10.7);
# ■ Вывод отсортированного списка оценок: по возрастанию или убыванию.

# def avg(num_list):  # вычисление среднеарифметического из списка чисел
#     if len(num_list) == 0:
#         raise ZeroDivisionError
#     return sum(num_list) / len(num_list)
#
#
# def input_handler(str_list):  # обработчик ввода
#     re_0 = re.compile(r'\d+\s*,\s*\d+\s*,\s*\d+\s*,\s*\d+\s*,\s*\d+\s*,'
#                       r'\s*\d+\s*,\s*\d+\s*,\s*\d+\s*,\s*\d+\s*,\s*\d+\s*')
#     str_list = re_0.findall(input_list)[0].split(',')
#     input_list_nums = []
#     for i in range(len(str_list)):
#         input_list_nums.append(int(str_list[i].strip()))
#     return input_list_nums
#
# while True:
#     input_list = input('Введите 10 оценок студента от 1 до 12 через запятую: ')
#     # input_list = [10, 12, 11, 12, 12, 12, 12, 9, 10, 12]
#
#     uncorrect_list = [num for num in input_handler(input_list) if num <= 0 or num > 12]
#
#     if len(uncorrect_list) > 0:
#         print(f'Некорректные данные: {uncorrect_list}')
#     else:
#         break
#
# while True:
#     print('''Введи следующий код запроса:
#                 score - вывод всех оценок этого ботаника;
#                 n, s - пересдача экзамена (введи номер оценки n в списке и новую оценку s);
#                 money - выходит ли стипендия (стипендия выходит, если средний балл не ниже 10.7);
#                 min..max - вывод отсортированного списка оценок по возрастанию;
#                 max..min - вывод отсортированного списка оценок по убыванию.''')
#
#     input_request = input()
#
#     re_1 = re.compile(r'score', re.IGNORECASE)
#     re_2 = re.compile(r'(\d+)\s*,\s*(\d+)')
#     re_3 = re.compile(r'money', re.IGNORECASE)
#     re_4 = re.compile(r'min..max', re.IGNORECASE)
#     re_5 = re.compile(r'max..min', re.IGNORECASE)
#
#     if re_1.search(input_request) != None:
#         print(f'Оценки студента: {input_handler(input_list)}')
#
#     if re_2.search(input_request) != None:
#         new_list = list(input_handler(input_list))
#         if 0 < int(re_2.search(input_request).group(2)) <= 12:
#             new_list[int(re_2.search(input_request).group(1))] = int(re_2.search(input_request).group(2))
#         print(f'Обновлённый список оценок студента: {new_list}')
#
#     if re_3.search(input_request) != None and avg(input_handler(input_list)) >= 10.7:
#         print(f'Стипендия будет:), средний балл {avg(input_handler(input_list))}')
#     elif re_3.search(input_request) != None and avg(input_handler(input_list)) < 10.7:
#         print(f'Стипендии не будет:(, средний балл {avg(input_handler(input_list))}')
#
#     if re_4.search(input_request) != None:
#         sorted_to_max = sorted(input_handler(input_list))
#         print(f'Сортировка оценок по возрастанию: {sorted_to_max}')
#
#     if re_5.search(input_request) != None:
#         sorted_to_min = sorted(input_handler(input_list), reverse=True)
#         print(f'Сортировка оценок по убыванию: {sorted_to_min}')


# Задача 3. Написать программу, реализующую сортировку списка методом усовершенствованной сортировки пузырьковым
# методом. Усовершенствование состоит в том, чтобы анализировать количество перестановок на каждом шагу, если
# это количество равно нулю, то продолжать сортировку нет смысла — список отсортирован.

# unsorted_list = [10, 122, 0, 12, 12, -100, 12, 9, 44, -212, 47]
#
#
# def mod_bubble_fun(some_list, direction):  # функция сортировки пузырьком
#     try:
#         if direction.strip() == 'в' or direction.strip() == 'у':
#             res_list = some_list.copy()
#             flag = True
#             while flag:
#                 flag = False
#                 for i in range(len(res_list) - 1):
#                     if res_list[i] > res_list[i + 1]:
#                         flag = True
#                         res_list[i], res_list[i + 1] = res_list[i + 1], res_list[i]
#             return res_list if direction.strip() == 'в' else res_list[::-1]
#     except:
#         print('В общем, как обычно, что-то пошло нет так..')
#
#
# print(mod_bubble_fun(unsorted_list, 'в'))
