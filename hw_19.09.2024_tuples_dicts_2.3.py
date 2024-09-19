# КОРТЕЖИ, МНОЖЕСТВА, СЛОВАРИ. ЧАСТЬ 2.

# Задание 3. Создайте программу «Фирма». Нужно хранить информацию о человеке: ФИО, телефон, рабочий email,
# название должности, номер кабинета, skype. Требуется реализовать возможность добавления, удаления,
# поиска, замены данных. Используйте словарь для хранения информации.

employees = [
    {'name': 'Дмитрий',
     'last name': 'Дмитров',
     'patronymic': 'Дмитриевич',
     'post': 'директор',
     'cabinet': '1',
     'tel': '8-916-900-99-99',
     'email': 'dmitrov@firma.ru',
     'skype': 'live:dmitrov'
     },
    {'name': 'Аграфена',
     'last name': 'Грушина',
     'patronymic': 'Сергеевна',
     'post': 'секретарь',
     'cabinet': '0',
     'tel': '8-916-700-00-16',
     'email': 'grusha@firma.ru',
     'skype': 'live:grusha'
     },
    {'name': 'Андрей',
     'last name': 'Федурнов',
     'patronymic': 'Алексеевич',
     'post': 'инженер',
     'cabinet': '13',
     'tel': '8-916-802-33-69',
     'email': 'fedurnov@firma.ru',
     'skype': 'live:fedurnov'
     },
]


def adder_fun(name, last_name, patronymic, post, cabinet, tel, email, skype, some_list):
    new_dict = {
        'name': name,
        'last name': last_name,
        'patronymic': patronymic,
        'post': post,
        'cabinet': cabinet,
        'tel': tel,
        'email': email,
        'skype': skype,
    }
    some_list.append(new_dict)
    return some_list


def del_fun(post, some_list):
    for i in range(len(some_list)):
        if some_list[i]['post'] == post:
            del some_list[i]
            return


def replacer_fun(post, old_val, new_val, some_list):
    for i in range(len(some_list)):
        if some_list[i]['post'] == post:
            for k, v in some_list[i].items():
                if v == old_val:
                    some_list[i][k] = new_val
                    return


def searcher_fun(last_name, some_list):
    for i in range(len(some_list)):
        if last_name.title() in some_list[i].values():
            print(f'===========================================\n'
                  f'Имя: {some_list[i].get('name', '').title()}\n'
                  f'Фамилия: {some_list[i].get('last name', '').title()}\n'
                  f'Отчество: {some_list[i].get('patronymic', '').title()}\n'
                  f'Должность: {some_list[i].get('post', '')}\n'
                  f'Кабинет: {some_list[i].get('cabinet', '')}\n'
                  f'Телефон: {some_list[i].get('tel', '')}\n'
                  f'Электронная почта: {some_list[i].get('email', '')}\n'
                  f'Скайп: {some_list[i].get('skype', '')}\n')


def display_fun(some_list):
    for i in range(len(some_list)):
        print(f'*******************************************\n'
              f'Имя: {some_list[i].get('name', '').title()}\n'
              f'Фамилия: {some_list[i].get('last name', '').title()}\n'
              f'Отчество: {some_list[i].get('patronymic', '').title()}\n'
              f'Отчество: {some_list[i].get('post', '')}\n'
              f'Кабинет: {some_list[i].get('cabinet', '')}\n'
              f'Телефон: {some_list[i].get('tel', '')}\n'
              f'Электронная почта: {some_list[i].get('email', '')}\n'
              f'Скайп: {some_list[i].get('skype', '')}\n')


flag = True

while flag:
    print('''\nВведите код операции:
    1 - внести данные о новом сотруднике
    2 - удалить данные о сотруднике
    3 - замена данных сотрудника
    4 - поиск сотрудника по фамилии
    d - вывести информацию о всех сотрудниках
    q - выход из приложения
    ''')

    input_num = input()

    if input_num.strip() == '1':
        in_name = input('Введите имя нового сотрудника: ')
        in_last_name = input('Введите фамилию нового сотрудника: ')
        in_patronymic = input('Введите отчество нового сотрудника: ')
        in_post = input('Введите пост нового сотрудника: ')
        in_cabinet = int(input('Введите номер кабинета нового сотрудника: '))
        in_tel = input('Введите телефонный номер нового сотрудника: ')
        in_email = input('Введите адрес электронной почты нового сотрудника: ')
        in_skype = input('Введите скайп нового сотрудника: ')

        adder_fun(in_name, in_last_name, in_patronymic, in_post, in_cabinet, in_tel, in_email, in_skype, employees)

    if input_num.strip() == '2':
        in_post = input('Введите должность сотрудника, которого удалить из базы: ')
        del_fun(in_post.strip().lower(), employees)

    if input_num.strip() == '3':
        in_post = input('Введите должность сотрудника для работы по замене данных: ')
        in_old_val = input('Что будем менять?: ')
        in_new_val = input('На что будем менять?: ')
        replacer_fun(in_post, in_old_val, in_new_val, employees)

    if input_num.strip() == '4':
        in_last = input('Введите фамилию сотрудника для поиска: ')
        searcher_fun(in_last, employees)

    if input_num.strip() == 'd':
        display_fun(employees)

    if input_num.strip() == 'q':
        flag = False
