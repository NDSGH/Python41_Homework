# Задание 06d.

# 1. Прочитать про предпосылки введения декораторов в Python
# https://peps.python.org/pep-0318/

# 2. Прочитать про декоратор @staticmethod
# https://docs.python.org/3/library/functions.html#staticmethod

# 3. Напишите (как вы поняли) возможную причину добавления декоратора @staticmethod в язык Python

# Статические методы не имеют доступа ни к атрибутам класса, ни к атрибутам его экземпляров. Это незвисимая функция.
# Декоратор @staticmethod добавлен для удобства работы с кодом. Если существует логическая связь между функцией и
# работой кода, то её можно не выносить за пределы класса (не создавать отдельную функцию), а придерживаться
# парадигме ООП и оставить её внутри класса.

# 4. Напишите простой и минималистичный пример демонстрирующий пользу декоратора @staticmethod

class BMI:
    """
    Класс для определения индекса массы тела.
    Здесь: m - масса (кг), h - рост (м).
    """
    def __init__(self, m, h):
        self.m = m
        self.h = h

    def calculate_bmi(self):
        bmi = self.m / pow(self.h, 2)
        print(bmi)

    @staticmethod
    def print_conclusion(num):
        if 1 < num <= 16:
            print('Выраженный дефицит массы тела')
        elif 16 < num <= 18.5:
            print('Дефицит массы тела')
        elif 18.5 < num <= 25:
            print('Норма')
        elif 25 < num <= 30:
            print('Избыточная масса тела')
        elif 30 < num <= 35:
            print('Ожирение 1 степени')
        elif 35 < num <= 40:
            print('Ожирение 2 степени')
        elif 40 < num < 100:
            print('Ожирение 3 степени')
        else:
            print('Проверьте правильность ввода bmi')


obj = BMI(80, 1.85)  # объект - человек
obj.calculate_bmi()  # индекс массы тела человека

BMI.print_conclusion(25)  # назависимый статический метод - подсказка по bmi


# 5. Вспомните про класс socket из библиотеки socket
# https://medium.com/@stephen.biston/write-an-http-server-from-the-ground-up-in-9-minutes-with-python-1fdb9800a26a

# 6. Ознакомьтесь с классом HTTPServer из модуля http.server
# https://realpython.com/python-http-server/
# https://docs.python.org/3/library/http.server.html

# 7. Полистайте документацию веб-фреймворка Flask
# https://flask.palletsprojects.com/en/stable/quickstart/






