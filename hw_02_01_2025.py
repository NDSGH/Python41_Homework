# Реализовать вручную алгоритм функции reduce. Создать и протестировать функцию reduce на примере нахождения
# суммы всех элементов списка.

from functools import reduce

num_list = [1, 2, 3, 4, 5]  # исходный список


class Reduce:
    def __init__(self, some_list, start=0):
        self.some_list = some_list
        self.start = start

    def add(self, acc, par):
        return acc + par

    def reduce_custom(self):
        """Основной метод"""
        res = self.start
        for val in self.some_list:
            res = self.add(res, val)
        return res

    def reduce_built(self):
        """Проверочный метод"""
        res = reduce(lambda acc, val: acc + val, self.some_list, self.start)
        return res


reduce_1 = Reduce(num_list, 5)  # создадим объект класса Reduce(список, начальное значение)

print('Результат основного метода: {}'.format(reduce_1.reduce_custom()))
print('Результат проверочного метода: {}'.format(reduce_1.reduce_built()))
