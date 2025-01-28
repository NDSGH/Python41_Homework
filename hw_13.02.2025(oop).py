print('================================= Наследование ================================')

# Задание 06а. Напишите класс Animal с методом walk. Напишите класс Bird наследованный от Animal с методом fly.
# Заставьте птицу ходить.


class Animal:
    def walk(self, creature):
        print(f'{creature} walking')


class Bird(Animal):
    def fly(self, creature):
        print(f'{creature} flying')


Bird().walk('bird')


print('================================= Класс как объект ================================')

# Задание 06b. Напишите класс IteratorClass который выдает значения от 0 до N-1 при каждом вызове метода next()
# от экземпляра класса. Значение N передавайте при инициализации класса через __init__(...).
# После того как итерация до N-1 завершилась -- возвращайте None при каждом вызове next().


# class IteratorClass:
#     i = 0
#
#     def __init__(self, n):
#         self.n = n
#
#     def next(self):
#         if self.i < self.n:
#             self.i += 1
#             return self.i - 1
#         else:
#             return None


class IteratorClass:
    def __init__(self, n):
        self.n = n
        self.start = 0

    def next(self):
        if self.start < self.n:
            self.start += 1
            return self.start - 1
        else:
            return None


iter1 = IteratorClass(4)
print(iter1.next())
print(iter1.next())
print(iter1.next())
print(iter1.next())
print(iter1.next())
