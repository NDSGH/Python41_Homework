# Задание 06c.

# 1-a) Напишите программу, которая ожидает ввода числа и после этого выводит его в консоль в двоичной,
# восьмеричной и шестнадцатеричной системе счисления, после чего ожидает повторного ввода числа.

# 1-б) Доработайте программу, чтобы она корректно обрабатывала нажатие клавиш Ctrl+C и выходила из цикла,
# выводя в консоль строку goodbye. Используйте try-except для класса ошибок KeyboardInterrupt.

# 1-с) Доработайте программу для случая, когда пользователь вводит данные, которые невозможно интерпретировать
# как число -- в этом случае программа должна выбросить исключение. Выбрасывайте исключения с помощью ключевого
# слова raise, а для указания типа исключения используйте класс ValueError

# print('*' * 20 + ' Задача 1 ' + '*' * 20)
#
#
# class Converter:
#     "Converter int to bin, oct, hex"
#     def __init__(self, number):
#         self.number = number
#
#     def __del__(self):
#         pass
#
#     def int_to_bin(self):
#         return format(self.number, 'b')
#         # return bin(number)[2:]
#
#     def int_to_oct(self):
#         return format(self.number, 'o')
#         # return oct(number)[2:]
#
#     def int_to_hex(self):
#         return format(self.number, 'x')
#         # return hex(number)[2:]
#
#
# while True:
#     try:
#         num = int(input('Введите целое десятичное число: '))
#
#         conv = Converter(num)
#
#         num_bin = conv.int_to_bin()
#         num_oct = conv.int_to_oct()
#         num_hex = conv.int_to_hex()
#
#         print(f'Двоичное число: {num_bin}\nВосьмеричное число: {num_oct}\nШестнадцатеричное число: {num_hex}\n')
#
#     except KeyboardInterrupt:
#         print('\ngoodbye')
#         break
#
#     except ValueError:
#         print('Данные должны быть числом!')


# 2. Напишите программу, которая:
#   - создает и присваивает переменной str (utf-8 string) строку "мама мыла раму"
#   - создает переменную str_b типа bytes (*) в которую помещает строку в виде байтов из переменной str,
#     используя информацию что строка в кодировке utf-8
#   - создает переменную str_i_arr в которую сохраняет массив байт из str_b в виде массива чисел
#   - выводит в консоль каждый элемент str_i_arr через запятую:
#     str_i_arr = 208, 188, 208, 176, 208, 188, 208, 176, 32, 208, 188, 209, 139, 208, 187, 208, 176, 32, 209, 128,
#     208, 176, 208, 188, 209, 131

# print('*' * 20 + ' Задача 2 ' + '*' * 20)
#
#
# class Bytes:
#     def __init__(self, str):
#         self.str = str
#
#     def str_to_bytes(self):
#         str_b = bytes(self.str, 'utf-8')
#         return str_b
#
#     def gen_byte_list(self):
#         str_i_arr = [int(byte) for byte in self.str_to_bytes()]
#         return str_i_arr
#
#     def print_bytes(self):
#         print('str_i_arr = ', end='')
#         for i, v in enumerate(self.gen_byte_list()):
#             print(v, end=', ' if i < len(str_i_arr) - 1 else '')
#
#
# obj = Bytes('мама мыла раму')
#
# str_b = obj.str_to_bytes()
#
# str_i_arr = obj.gen_byte_list()
#
# obj.print_bytes()


# 3. Напишите программу, которая ожидает ввода (utf-8) строки, после чего заносит ее в
# переменную str (тип utf-8 string).
# Затем объявите переменную str_bytes (тип bytes) и присвойте ей значение строки str в виде массива байт.
# Подсчитайте кол-во символов str, кол-во байт str_bytes.
# Выведите информацию о кол-ве символов и байт в консоль, а так же выведите в консоль str_bytes в виде
# последовательности чисел от 0 до 255 (например: str_bytes=93,26,105,32,67).

print('*' * 20 + ' Задача 3 ' + '*' * 20)

# str_ = input('Введите строку: ')
#
# str_bytes = [int(byte) for byte in bytes(str_, 'utf-8')]
#
# print(f'Количество символов str_: {len(str_)}, количество байт str_bytes: {len(str_bytes)}')
#
# print('str_bytes = ', end='')
# for i, v in enumerate(str_bytes):
#     print(v, end=', ' if i < len(str_bytes) - 1 else '')


class Bytes2:
    def __init__(self, str_):
        self.str_ = str_

    def gen_bytes_list(self):
        str_bytes = [int(byte) for byte in bytes(self.str_, 'utf-8')]
        return str_bytes

    def print_number_of_symbols_bytes(self):
        print(f'Количество символов str_: {len(self.str_)}, количество байт str_bytes: {len(self.gen_bytes_list())}')

    def print_bytes_in_row(self):
        print('str_bytes = ', end='')
        for i, v in enumerate(self.gen_bytes_list()):
            print(v, end=', ' if i < len(self.gen_bytes_list()) - 1 else '')
        print()


while True:
    try:
        str_ = input('\nВведите строку: ')

        obj_ = Bytes2(str_)
        obj_.print_number_of_symbols_bytes()
        obj_.print_bytes_in_row()

    except KeyboardInterrupt:
        print(f'\nВыход из программы!')
        break
