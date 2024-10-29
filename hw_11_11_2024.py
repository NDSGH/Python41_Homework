# Создать и протестировать функцию, которая принимает массив чисел (числа в массиве могут повторяться)
# и определяет наиболее часто встречающийся элемент массива

num_list_in = [112, -555, 1000, 155, 112, 112, -555, -1, 0, 22, 22, 22, 8, 8, 8]


def friq_num_1(num_list):
    """
    :param num_list: number list
    :return: list with value(s) with maximum repetition
    """
    try:
        num_set = set(num_list)  # уникальные значения
        c_list = []  # список значений счётчика повторений
        v_list = []  # список чисел
        for i, v in enumerate(num_set):
            c_list.append(num_list.count(v))
            v_list.append(v)

        c_list_max = []  # список счётчика максимума повторений
        i_list_max = []  # список индексов
        v_list_max = []  # список максимальных значений
        for ind, num in enumerate(c_list):
            if num == max(c_list):
                c_list_max.append(num)
                i_list_max.append(ind)
                v_list_max.append(v_list[ind])

        if len(c_list_max) > 1:
            print(f'В списке чисел {v_list} максимальное количество повторений приходится'
                  f' на значения с индексами: {i_list_max}.'
                  f' Число повторений: {max(c_list)}')
        else:
            print(f'В списке чисел {v_list} максимальное количество повторений приходится'
                  f' на значение с индексом: {i_list_max}.'
                  f' Число повторений: {max(c_list)}')

        return v_list_max

    except BaseException:
        print('Error. Check input data')
        return None

def friq_num_2(num_list):
    """
    :param num_list: number list
    :return: list with value(s) with maximum repetition
    """
    try:
        num_set = list(set(num_list))  # уникальные значения
        dict_set = {i: num_list.count(v) for i, v in enumerate(num_set)}
        key_list_max = []
        val_list_max = []
        for k, val in dict_set.items():
            if val == max(dict_set.values()):
                key_list_max.append(k)
                val_list_max.append(num_set[k])

        print(f'В списке чисел {num_set} максимальное количество повторений приходится'
              f' на значени{'я' if len(key_list_max) > 1 else 'е'}'
              f' с индекс{'ами' if len(key_list_max) > 1 else 'ом'}: {key_list_max}.'
              f' Число повторений: {dict_set[key_list_max[0]]}')

        return val_list_max

    except BaseException:
        print('Error. Check input data')
        return None


# print(friq_num_1(num_list_in))
# print()
# print(friq_num_2(num_list_in))
