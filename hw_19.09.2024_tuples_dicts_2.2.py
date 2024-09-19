# КОРТЕЖИ, МНОЖЕСТВА, СЛОВАРИ. ЧАСТЬ 2.

# Задание 2. Создайте программу «Англо-французский словарь». Нужно хранить слово на английском языке
# и его перевод на французский. Требуется реализовать возможность добавления, удаления, поиска, замены данных.
# Используйте словарь для хранения информации.

en_fr_dict = {
    'dog': 'chien',
    'cat': 'chat',
    'rabbit': 'lapin',
    'parrot': 'perroquet',
    'snake': 'serpent'
}


def adder_to_dict(new_key, new_val, some_dict):
    if new_key.isalpha() and new_val.isalpha():
        some_dict[new_key.lower()] = new_val.lower()
    else:
        print('Некорректный ввод!')
    return some_dict


def replacer_dict(old_key, new_key, new_val, some_dict):
    if old_key in some_dict and new_key.isalpha() and new_val.isalpha():
        del some_dict[old_key]
        some_dict[new_key] = new_val
    else:
        print('Некорректный ввод!')
    return some_dict


flag = True

while flag:
    print('''\nВведите код операции со словарём:
    1 - получение перевода английского слова
    2 - добавление нового слова в словарь
    3 - удаление слова из словаря
    4 - замена слова в словаре
    5 - поиск английского слова в словаре
    6 - поиск французского слова в словаре
    d - показать содержимое словаря
    q - выход из приложения
    ''')

    input_num = input()

    if input_num.strip() == '1':
        en_word = input('Введите слово на английском: ')
        if en_word.strip() in en_fr_dict:
            print(f'\nСлово (en) - {en_word}, перевод (fr) - {en_fr_dict[en_word]}')

    if input_num.strip() == '2':
        new_en_word = input('Введите новое английское слово: ')
        new_fr_word = input('Введите перевод на французский: ')
        adder_to_dict(new_en_word, new_fr_word, en_fr_dict)

    if input_num.strip() == '3':
        rem_word = input('Введите удаляемое из словаря английское слово: ')
        if rem_word in en_fr_dict:
            del en_fr_dict[rem_word]

    if input_num.strip() == '4':
        rep_word_1 = input('Введите заменяемое английское слово: ')
        rep_word_2 = input('Введите новое английское слово: ')
        rep_word_3 = input('Введите перевод: ')
        replacer_dict(rep_word_1, rep_word_2, rep_word_3, en_fr_dict)

    if input_num.strip() == '5':
        sch_word = input('Введите английское слово для поиска: ')
        if sch_word.strip() in en_fr_dict:
            print(f'\nСлово (en) - {sch_word.strip()}, перевод (fr) - {en_fr_dict[sch_word.strip()]}')

    if input_num.strip() == '6':
        sch_fr_word = input('Введите французское слово для поиска: ')
        for k, v in en_fr_dict.items():
            if v == sch_fr_word.strip():
                print(f'\nСлово (en) - {k}, перевод (fr) - {v}')

    if input_num.strip() == 'd':
        for k, v in en_fr_dict.items():
            print(f'Слово (en) - {k}, перевод (fr) - {v}')

    if input_num.strip() == 'q':
        flag = False
