import re


class FunnyRegex:
    def __init__(self, some_string):
        self.some_string = some_string

    def splitter(self, sep):
        split_regex = re.split(fr'{sep}', str(self.some_string))
        print(f'Разделитель: "{sep}"')
        for elem in split_regex:
            print(elem)
        print()

    def replaser(self, rep):
        rep_regex = re.sub(r' ', f'{rep}', f'{self.some_string.strip()}')
        print(rep_regex)
        print()


# 1. используя re.split разбить строку по нескольким разделителям (запятая, точка с запятой, пробел)

s_1 = 'яблоко,банан;груша апельсин'

splitRegex = FunnyRegex(s_1)
splitRegex.splitter(',')
splitRegex.splitter(';')
splitRegex.splitter(' ')


# 2.  используя re.sub замените все пробелы на подчёркивания и уберите пробелы в начале и конце строки

s_2 = ' Это пример текста с пробелами '

repRegex = FunnyRegex(s_2)
repRegex.replaser('_')
