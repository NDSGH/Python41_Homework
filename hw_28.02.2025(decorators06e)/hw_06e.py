# Задание 06-e


# а) напишите декоратор fun_decorator который добавит ф-ии в словарь по передаваемому в декоратор ключу.

# б) Перепишите тела функций my_function1 и my_function2, чтобы они выводили что-нибудь в консоль;
# а затем вызовите обе функции поочередно используя словарь my_dict

my_dict = {}


def fun_decorator(arg):
    def wrap(f):
        my_dict[arg] = f
    return wrap


@fun_decorator('key1')
def my_function1():
    print('Hi, I am function 1')


@fun_decorator('key2')
def my_function2():
    print('Hi, I am function 2')


for val in my_dict.values():
    val()
