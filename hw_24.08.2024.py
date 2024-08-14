# Задание 1. Пользователь вводит с клавиатуры номер дня недели (1-7). Необходимо вывести на экран
# названия дня недели. Например, если 1, то на экране надпись понедельник, 2 - вторник и т. д.
try:
    day_of_week = int(input('Введите номер для недели (1..7): '))
    if day_of_week == 1:
        print('Понедельник')
    elif day_of_week == 2:
        print('Вторник')
    elif day_of_week == 3:
        print('Среда')
    elif day_of_week == 4:
        print('Четверг')
    elif day_of_week == 5:
        print('Пятница')
    elif day_of_week == 6:
        print('Суббота')
    elif day_of_week == 7:
        print('Воскресенье')
    else:
        print('Число должно быть в диапазоне 1..7')
except BaseException as err:
    print('Вы должны ввести число, прошу быть внимательнее!')
    print(err)


# Задание 2. Пользователь вводит с клавиатуры номер месяца (1-12). Необходимо вывести на экран название месяца.
# Например, если 1, то на экране надпись январь, 2—февраль и т.д.
# try:
#     month = int(input('Введите номер месяца (1..12): '))
#     if month == 1:
#         print('Январь')
#     elif month == 2:
#         print('Февраль')
#     elif month == 3:
#         print('Март')
#     elif month == 4:
#         print('Апрель')
#     elif month == 5:
#         print('Май')
#     elif month == 6:
#         print('Июнь')
#     elif month == 7:
#         print('Июль')
#     elif month == 8:
#         print('Август')
#     elif month == 9:
#         print('Сентябрь')
#     elif month == 10:
#         print('Октябрь')
#     elif month == 11:
#         print('Ноябрь')
#     elif month == 12:
#         print('Декабрь')
#     else:
#         print('Число должно быть в диапазоне 1..12')
# except ValueError as err:
#     print('Вы должны ввести число, следите за пальцами!!')
#     print(err)


# Задание 3. Пользователь вводит с клавиатуры число. Если число больше нуля нужно вывести
# надпись «Number is positive», если меньше нуля «Number is negative», если равно нулю «Number is equal to zero»
# try:
#     num = int(input('Input a number: '))
#     if num > 0:
#         print('Number is positive')
#     elif num < 0:
#         print('Number is negative')
#     else:
#         print('Number is equal to zero')
# except:
#     print('What is that mean! You should input a number! Try again!')


# Задание 4. Пользователь вводит два числа. Определить, равны ли эти числа, и, если нет,
# вывести их на экран в порядке возрастания.
# try:
#     x = int(input('Input a first number: '))
#     y = int(input('Input a second number: '))
#     if x == y:
#         print('This numbers are equal')
#     elif x < y:
#         print(x, y)
#     else:
#         print(y, x)
# except:
#     print('Incorrect input. Try again!')
