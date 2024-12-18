# Создать рекурсивную функцию filtr для фильтрации массива. Функция filtr принимает функцию f и массив и возвращает
# в результате массив, состоящий из тех элементов, для которых функция f возвращает истину.


num_list = [-89, 0, -1, 2, 3, 4, -5]  # исходный список чисел


def f(x):
    return x >= 0

# Вариант 1
# def filtr(func, number_list, arr=[]):
#     if len(number_list) == 0:  # базовый случай
#         return arr
#     else:  # рекурсивный случай
#         if func(number_list[0]):
#             arr.append(number_list[0])
#         return filtr(func, number_list[1:], arr)
    
    
# Вариант 2
def filtr(func, number_list):
    if len(number_list) == 0:  # базовый случай
        return []
    else:  # рекурсивный случай
        if func(number_list[0]):
            return [number_list[0]] + filtr(func, number_list[1:])
        else:
            return filtr(func, number_list[1:])
    
    

    


print(filtr(f, num_list))
