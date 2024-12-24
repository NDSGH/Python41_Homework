# Реализовать вручную алгоритм функции reduce. Создать и протестировать функцию reduce на примере нахождения
# суммы всех элементов списка.

from functools import reduce

num_list = [1, 2, 3, 4, 5]  # исходный список


class Reduce:
    def __init__(self, some_list, op='+', start=0):
        self.some_list = some_list
        self.start = start
        self.op = op

    def func(self, acc, val):
        """Функция для работы основного метода reduce"""
        return eval(f'{acc}{self.op}{val}')
    
    def reduce_custom(self):
        """Основной метод reduce"""
        res = self.start
        for val in self.some_list:
            res = self.func(res, val)
        return res
    
    def reduce_built(self):
        """Проверочный метод reduce"""
        res = reduce(lambda acc, val: eval(f'{acc}{self.op}{val}'), self.some_list, self.start)
        return res


reduceObj = Reduce(num_list, '+', 5)  # объект класса Reduce(список, операция, нач. значение)

print('Результат основного метода: {}'.format(reduceObj.reduce_custom()))
print('Результат проверочного метода: {}'.format(reduceObj.reduce_built()))
