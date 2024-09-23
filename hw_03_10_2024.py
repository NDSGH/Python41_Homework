# Задание. Создать и протестировать ф-ю, которая принимает список и разворачивает порядок следования
# элементов списка (создать собственный алгоритм).

test_list = ['25', 'spades', '007', 'flag', 'Jack']


def reverser_fun_1(some_list=[]):
    """
    Get some list
    :return: new reversed list
    """
    if isinstance(some_list, list):
        reversed_list = []
        for i in range(len(some_list)):
            reversed_list.insert(0, some_list[i])
        return reversed_list


print(reverser_fun_1(test_list))


def reverser_fun_2(some_list=[]):
    """
    Get some list
    :return: new reversed list
    """
    if isinstance(some_list, list):
        reversed_list = [test_list[len(some_list) - 1 - i] for i in range(len(some_list))]
        return reversed_list


print(reverser_fun_2(test_list))


def reverser_fun_3(some_list=[]):
    """
    Get some list
    :return: new reversed list
    """
    if isinstance(some_list, list):
        return some_list[::-1]


print(reverser_fun_3(test_list))


# Для тестирования функций следует открыть и запустить файл unit_test_03_10_2024.
