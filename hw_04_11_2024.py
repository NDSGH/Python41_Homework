# Задание. Создать и протестировать функцию, которая принимает число и преобразует его в строку в двоичном
# представлении.

import math

num_test = -15  # тестовый аргумент


def int_to_bin_1(num):  # первая функция (собственный алгоритм)
    str_bin, res = '', abs(num)
    if res > 0:
        while res > 0:
            str_bin += str(res % 2)
            res = math.floor(res / 2)
        return str_bin[::-1] if num > 0 else '-' + str_bin[::-1]
    elif num == 0:
        return f'{num}'


def int_to_bin_2(num):  # вторая функция (применение функции format())
    return str(format(num, 'b'))


print(int_to_bin_1(num_test))
print(int_to_bin_2(num_test))
