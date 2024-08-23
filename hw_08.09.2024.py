# Задание. Дан список целых чисел. Создать и протестировать ф-ю, которая определяет количество чётных
# элементов в списке

some_list = [0, 101, 1005, 1, 0, 415, 7, 9, -2, 8, 4]  # исходный список

# Создадим функцию, определяющую количество чётных чисел в списке и протестируем её при помощи assert
# Тест проведём на тип агрумента и на тип данных элементов списка


def test_of_even(any_list):
    """
    This function takes a list of integers
    :return: amount of even numbers in list
    """

    assert isinstance(any_list, list), 'type of argument must be - list'

    for val in any_list:
        if not isinstance(val, int):
            assert False, 'type of elements must be - int'

    counter = 0
    for elem in any_list:
        if not elem % 2:
            counter += 1
    return counter


print(test_of_even(some_list))
