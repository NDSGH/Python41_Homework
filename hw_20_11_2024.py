# Создать и протестировать функцию, кот. принимает массив чисел (элементы в массиве могут повторяться) и удаляет
# повторяющиеся числа. В итоговом массиве каждое значение встречается только один раз.

num_list_in = [112, -555, 1000, 155, 112, 112, -555, -1, 0, 22, 22, 22, 8, 8, 8]


def set_fun_1(num_list):
    try:
        if isinstance(num_list, list) and num_list != []:
            num_list_sort = sorted(num_list)
            set_list = [num_list_sort[0]]
            for i in range(len(num_list_sort) - 1):
                if num_list_sort[i] != num_list_sort[i + 1]:
                    set_list.append(num_list_sort[i + 1])
            return set_list
    except:
        return None


def set_fun_2(num_list):
    try:
        if isinstance(num_list, list) and num_list != []:
            set_list = set(num_list)
            return sorted(list(set_list))
    except:
        return None


# print(set_fun_1(num_list_in))
# print(set_fun_2(num_list_in))
