# Создать и протестировать функцию, которая принимает массив чисел и выполняет его сортировку по возрастанию

number_list = [25, -1000, 0, 0, 152, 255, -96]  # исходный список


def bubble_sort(num_list):  # создадим усовершенствованную функцию сортировки пузырьком (вариант 1)
    num_list_copy = num_list.copy()
    flag = True
    while flag:
        flag = False
        for i in range(len(num_list_copy) - 1):
            if num_list_copy[i] > num_list_copy[i + 1]:
                flag = True
                num_list_copy[i], num_list_copy[i + 1] = num_list_copy[i + 1], num_list_copy[i]
    return num_list_copy


print(bubble_sort(number_list))


def inbuilt_sort(num_list):  # создадим ф-ю, повторяющую и проверяющую предыдущую ф-ю (вариант 2)
    sorted_list = sorted(num_list)
    return sorted_list


print(inbuilt_sort(number_list))
