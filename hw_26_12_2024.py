# Создать рекурсивную функцию filtr для фильтрации массива. Функция filtr принимает функцию f и массив и возвращает
# в результате массив, состоящий из тех элементов, для которых функция f возвращает истину.


num_list = [-89, 0, -1, 2, 3, 4, -5]  # исходный список чисел


def f(x):
    return x >= 0


def filtr(func, number_list, arr=[]):
    if len(number_list) == 0:  # базовый случай
        return arr
    else:  # рекурсивный случай
        if func(number_list[0]):
            arr.append(number_list[0])
        return filtr(func, number_list[1:], arr)


print(filtr(f, num_list))
