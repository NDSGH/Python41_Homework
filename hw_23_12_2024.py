# Создать функцию filtr для фильтрации массива. Функция filtr принимает функцию f и массив и возвращает
# в результате массив, состоящий из тех элементов, для которых функция f возвращает истину.
# Протестировать функцию filtr на примере удаления из массива отрицательных чисел.

import datetime
import traceback

num_list = [-89, 0, -1, 2, 3, 4, -5]  # исходный список чисел

try:
    def f(x):
        return x >= 0


    def filtr(func, number_list):
            new_list = []
            for num in number_list:
                if func(num):
                    new_list.append(num)
            return new_list


    res_list_1 = filtr(f, num_list)  # результат работы основной функции
    res_list_2 = [num for num in num_list if f(num)]  # результат работы проверочного кода 1
    res_list_3 = list(filter(lambda x: x >= 0, num_list))  # результат работы проверочного кода 2

    print(f'Исходный массив чисел: {num_list}')
    print(f'Результат работы основной функции: {res_list_1}')
    print(f'Результат работы проверочного кода 1: {res_list_2}')
    print(f'Результат работы проверочного кода 2: {res_list_3}')


except:
    dt = datetime.datetime.now()
    errFile = open('err_log.txt', 'a')
    errFile.write(f'{dt}\n')
    errFile.write(traceback.format_exc())
    errFile.write('\n\n')
    errFile.close()
    print('Ошибка! Стек вызовов записан в файл err_log.txt')
