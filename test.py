# Задание. Создать программу, которая принимает последовательность чисел через аргументы командной строки и нахоидит их сумму.
# Например: python test.py 1 2 3 4 5 res = 15

import sys


def adder_nums_cmd(args):
    try:
        str_list = args[1:]
        num_list = []
        for arg in str_list:
            num_list.append(int(arg))
        return sum(num_list)
    except Exception as e:
        print(e)
        return None

print(f'res = {adder_nums_cmd(sys.argv)}')
