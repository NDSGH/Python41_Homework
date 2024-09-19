# КОРТЕЖИ, МНОЖЕСТВА, СЛОВАРИ. ЧАСТЬ 2.

import re
import sys

# Задание 1. Создайте программу, хранящую информацию о великих баскетболистах. Нужно хранить ФИО баскетболиста
# и его рост. Требуется реализовать возможность добавления, удаления, поиска, замены данных. Используйте словарь
# для хранения информации.

bb_players = [
    {'name': 'Сергей',
     'last name': 'Белов',
     'patronymic': 'Александрович',
     'height': 190
     },
    {'name': 'Владимир',
     'last name': 'Ткаченко',
     'patronymic': 'Петрович',
     'height': 220
     },
    {'name': 'Александр',
     'last name': 'Белов',
     'patronymic': 'Александрович',
     'height': 200
     },
    {'name': 'Алексей',
     'last name': 'Швед',
     'patronymic': 'Викторович',
     'height': 198
     },
    {'name': 'Сергей',
     'last name': 'Базаревич',
     'patronymic': 'Валерианович',
     'height': 191
     },
]


re_0 = re.compile(r'[а-яА-Я]{2,}', re.IGNORECASE)  # фильтруем ФИО
re_1 = re.compile(r'[0-9]{3}')  # фильтруем рост
re_2 = re.compile(r'[0-9]')  # фильтруем индекс


while True:
    print('''
            Приветствую на информационном портале "Великий баскетболист"!
            Для получения информации, введите цифру (для выхода нажмите любую клавишу):
                1 - вывести информацию о всех баскетболистах из базы данных;
                2 - загрузить в базу информацию о новом игроке;
                3 - удалить из базы информацию об игроке;
                4 - найти игрока по имени.
    ''', end='\n\n')

    input_num = input()

    if input_num.strip() == '1':
        for i in range(len(bb_players)):
            print(f'{bb_players[i].get('name', '').title()} {bb_players[i].get('patronymic', '').title()} '
                  f'{bb_players[i].get('last name', '').title()}, рост {bb_players[i].get('height', '')}')
    elif input_num.strip() == '2':
        bb_players.append({})
        new_name = input('Введите имя нового игрока: ')
        new_last_name = input('Введите фамилию нового игрока: ')
        new_patronymic = input('Введите отчество нового игрока: ')
        new_height = input('Введите рост нового игрока: ')
        if re_0.search(new_name):
            bb_players[len(bb_players) - 1]['name'] = new_name.strip().capitalize()
        if re_0.search(new_last_name):
            bb_players[len(bb_players) - 1]['last name'] = new_last_name.strip().capitalize()
        if re_0.search(new_patronymic):
            bb_players[len(bb_players) - 1]['patronymic'] = new_patronymic.strip().capitalize()
        if re_1.search(new_height):
            bb_players[len(bb_players) - 1]['height'] = int(new_height.strip())
    elif input_num.strip() == '3':
        del_player = input('Введите индекс игрока, данные о котом нужно удалить (начиная с 0): ')
        if re_2.search(del_player):
            del bb_players[int(del_player.strip())]
    elif input_num.strip() == '4':
        search_player = input('Введите имя игрока для поиска: ')
        if re_0.search(search_player):
            for i in range(len(bb_players)):
                if search_player.title() in bb_players[i].values():
                    print(f'{bb_players[i].get('name', '')} {bb_players[i].get('patronymic', '')} '
                          f'{bb_players[i].get('last name', '')}, рост {bb_players[i].get('height', '')}')
    else:
        sys.exit()
