# Создать и протестировать функцию, которая принимает число и проверяет - является ли оно простым?

def is_prime(int_num):
    """
    input: int number >= 2
    return: True if arg is prime, False if arg is not prime, None else
    """
    if type(int_num) is not int:
        return None
    if int_num < 2:
        return False
    elif int_num >= 2:
        lim = int(pow(int_num, 0.5)) + 1
        gen = (num for num in range(2, lim) if int_num % num == 0)
        if len(list(gen)) == 0:
            return True
        else:
            return False
