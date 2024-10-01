# Задание. Создать и протестировать ф-ю, которая принимает список чисел и находит два максимальных
# значения в списке (создать собственный алгоритм).

# from random import randint

# num_list = [randint(-1000, 1000) for num in range(0, 10)]
# print(f'Исходный список: {num_list}')


def two_of_max_1(number_list):
    """main function"""
    copy_list = number_list.copy()
    flag = True
    while flag:
        flag = False
        for i in range(len(copy_list) - 1):
            if copy_list[i] > copy_list[i + 1]:
                flag = True
                copy_list[i], copy_list[i + 1] = copy_list[i + 1], copy_list[i]
    set_list = []
    for num in copy_list:
        if num not in set_list:
            set_list.append(num)
    return set_list[::-1][:2]


def two_of_max_2(number_list):
    """check function"""
    sorted_list = list(set(number_list))
    return sorted(sorted_list, reverse=True)[:2]


# print(f'Ответ ф-ции 1: {two_of_max_1(num_list)}')
# print(f'Ответ ф-ции 2: {two_of_max_2(num_list)}')


# Для тестирования функций, следует открыть и запустить файл unit_test_10_10_2024.
# Для простой проверки функций, следует раскомментировать код текущего приложения (в начале и конце).
