import re


class FunnyRegex:
    def __init__(self, some_string):
        self.some_string = some_string

    def phone_parser(self):
        phone_regex = re.finditer(r'\+7-(\d\d\d)-(\d\d\d-\d\d-\d\d)', str(self.some_string))
        for phone in phone_regex:
            print(f'Оператор: {phone[1]}, Номер: {phone[2]}')
        print()

    def html_parser(self):
        html_regex = re.finditer(r'<(\w+)>(\w*)</\w+>', str(self.some_string))
        for tag in html_regex:
            print(f'Тег: {tag[1]}, Содержимое: {tag[2]}')
        print()

    def money_parser(self):
        money_regex = re.finditer(r'(\d+)\s*(\w+\.?)', str(self.some_string))
        for m in money_regex:
            print(f'Сумма: {m[1]}, Валюта: {m[2]}')
        print()

    def url_parser(self):
        url_regex = re.finditer(r'\b(http(s)?)://(\w+\.\w+)(/\w+)', str(self.some_string))
        for url in url_regex:
            print(f'Протокол: {url[1]}, Домен: {url[2]}, Путь: {url[3]}')
        print()


# 1. Парсинг номеров телефонов
# В тексте найти все телефонные номера в формате +7-XXX-XXX-XX-XX и вывести отдельно код оператора и сам номер.

s1 = 'Позвоните +7-999-123-45-67 или +7-812-555-12-34'

phoneRegex = FunnyRegex(s1)
phoneRegex.phone_parser()


# 2. Нахождение тегов HTML
# Найти в HTML-тексте все пары открывающего и закрыв. тега (например, <b>текст</b>) и вывести содержимое между ними.

s2 = '<b>жирный</b> и <i>курсив</i> текст'

tagRegex = FunnyRegex(s2)
tagRegex.html_parser()


# 3. Извлечение валют из строки
# В тексте найти все суммы в формате число + пробел + валюта и вывести отдельно сумму и валюту

s3 = 'Стоимость: 1200 USD, 9000 руб., 75 EUR.'

moneyRegex = FunnyRegex(s3)
moneyRegex.money_parser()


# 4. URL-парсер
# Разобрать строку с URL и выделить протокол, домен и путь.

s4 = 'Сайты: https://example.com/path, http://google.com/search'

urlRegex = FunnyRegex(s4)
urlRegex.url_parser()
