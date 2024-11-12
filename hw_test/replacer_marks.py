# Задание. Создать программу, которая перебирает все файлы с html разметкой в текущей папке и во всех файлах
# меняет тип метки. Например: старая метка: <!--#name-->, новая метка {{name}}

import os
import re

re_1 = re.compile(r'(<!--.?#.*-->)')  # looking for a mark in the markup <!--#content-->

re_2 = re.compile(r'(\{{2}.*?}{2})')  # looking for a mark in the markup {{ content }}

directory = '/hw_test'


def replacer_marks(n=1):
    """
    This function iterates through all files in current directory
    and replase all marks.
    Arguments: 1 - match to mark {{ name }}, 2 - match to mark <!--#name-->
    :return: new marks in all files in current directory
    """
    try:
        for filename in os.scandir(directory):
            if filename.is_file() and not filename.name == 'replacer_marks.py' and (n == 1 or n == 2):
                with open(filename, 'r') as f:
                    content = f.read()
                    re_list = re_1.findall(content) if n == 1 else re_2.findall(content)
                    if len(re_list) != 0:
                        for i in range(len(re_list)):
                            content = content.replace(re_list[i], '{{ ' + re_list[i].strip('<!-- #-->') + ' }}') \
                                if n == 1 else content.replace(re_list[i], '<!--#' + re_list[i].strip('{{ }}') + '-->')
                    with open(filename, 'w') as fw:
                        fw.write(content)
    except BaseException:
        print(f'Something went wrong...')


replacer_marks(1)  # choose mark type: 1 - {{ name }}, 2 - <!--#name-->
