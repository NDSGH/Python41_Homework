# КОРТЕЖИ, МНОЖЕСТВА, СЛОВАРИ. ЧАСТЬ 2.

# Задание 4. Создайте программу «Книжная коллекция». Нужно хранить информацию о книгах: автор, название книги,
# жанр, год выпуска, количество страниц, издательство. Требуется реализовать возможность добавления, удаления,
# поиска, замены данных. Используйте словарь для хранения информации.

books = [
    {'author': 'Стругацкий Аркадий, Стругацкий Борис',
     'title': 'Пикник на обочине',
     'genre': 'фантастика',
     'year': '2023',
     'pages': '192',
     'publishing house': 'АСТ',
     },
    {'author': 'Берроуз Эдгар Райс',
     'title': 'Принцесса Марса',
     'genre': 'фантастический роман',
     'year': '1992',
     'pages': '128',
     'publishing house': 'Советский композитор',
     },
    {'author': 'Дойл Артур Конан',
     'title': 'Приключения Шерлока Холмса',
     'genre': 'детектив',
     'year': '2023',
     'pages': '384',
     'publishing house': 'АСТ',
     },
]


def adder_fun(author, title, genre, year, pages, publishing_house, some_list):
    new_dict = {
        'author': author,
        'title': title,
        'genre': genre,
        'year': year,
        'pages': pages,
        'publishing house': publishing_house,
    }
    some_list.append(new_dict)
    return some_list


def del_fun(title, some_list):
    for i in range(len(some_list)):
        if some_list[i]['title'] == title.title():
            del some_list[i]
            return


def replacer_fun(title, old_val, new_val, some_list):
    for i in range(len(some_list)):
        if some_list[i]['title'].title() == title.title():
            for k, v in some_list[i].items():
                if v == old_val:
                    some_list[i][k] = new_val
                    return


def searcher_fun(title, some_list):
    for i in range(len(some_list)):
        if title.title() in some_list[i].values():
            print(f'===========================================\n'
                  f'Автор: {some_list[i].get('author', '').title()}\n'
                  f'Название: {some_list[i].get('title', '').title()}\n'
                  f'Жанр: {some_list[i].get('genre', '')}\n'
                  f'Год выпуска: {some_list[i].get('year', '')}\n'
                  f'Количество страниц: {some_list[i].get('pages', '')}\n'
                  f'Издательство: {some_list[i].get('publishing house', '')}\n')


def display_fun(some_list):
    for i in range(len(some_list)):
        print(f'*******************************************\n'
              f'Автор: {some_list[i].get('author', '').title()}\n'
              f'Название: {some_list[i].get('title', '').title()}\n'
              f'Жанр: {some_list[i].get('genre', '')}\n'
              f'Год выпуска: {some_list[i].get('year', '')}\n'
              f'Количество страниц: {some_list[i].get('pages', '')}\n'
              f'Издательство: {some_list[i].get('publishing house', '')}\n')


flag = True

while flag:
    print('''\nВведите код операции приложения "Книжная коллекция":
    1 - добавить новую книгу в коллекцию
    2 - удалить книгу из коллекции
    3 - заменить данные о книге
    4 - поиск книги по названию
    d - вывести информацию о всех книгах в коллекции
    q - выход из приложения
    ''')

    input_num = input()

    if input_num.strip() == '1':
        in_author = input('Введите ФИО автора: ')
        in_title = input('Введите название книги: ')
        in_genre = input('Введите жанр произведения: ')
        in_year = input('Введите год выпуска книги: ')
        in_pages = int(input('Введите количество страниц: '))
        in_publishing_house = input('Введите издательство: ')

        adder_fun(in_author, in_title, in_genre, in_year, in_pages, in_publishing_house, books)

    if input_num.strip() == '2':
        in_title = input('Введите название удаляемой книги: ')
        del_fun(in_title.strip().title(), books)

    if input_num.strip() == '3':
        in_title = input('Введите название книги для работы по замене данных: ')
        in_old_val = input('Что будем менять?: ')
        in_new_val = input('На что будем менять?: ')
        replacer_fun(in_title, in_old_val, in_new_val, books)

    if input_num.strip() == '4':
        in_title_ = input('Введите название книги для поиска: ')
        searcher_fun(in_title_, books)

    if input_num.strip() == 'd':
        display_fun(books)

    if input_num.strip() == 'q':
        flag = False
