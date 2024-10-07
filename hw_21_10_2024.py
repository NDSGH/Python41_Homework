# Создать и протестировать функцию, которая принимает число и проверяет - является ли оно простым.


def is_prime(in_num):
    """
    input: int number more than 2
    return: True if arg is prime, False if arg is not prime, None else
    """
    if type(in_num) is not int:
        return None
    elif in_num < 2:
        return None
    else:
        counter = 0
        for num in range(2, in_num):
            if in_num % num == 0:
                counter += 1
                if counter > 0:  # ускорит проверку при больших значениях
                    break
        res = True if counter == 0 else False
        return res
