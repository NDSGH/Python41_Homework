#!C:\Users\Dimm\AppData\Local\Programs\Python\Python312\python.exe

import json
import os
from urllib.parse import parse_qs

print('Content-type: text/html', end='\n\n')

with open('./pdd.html') as f:
    html = f.read()

with open('pdd.txt', 'r') as file:
    quest_data_json = file.read()  # читаем данные из файла pdd.txt

query_string = os.getenv('QUERY_STRING')

data = parse_qs(query_string)

quest_data = json.loads(quest_data_json)  # переводим тип данных из строки в массив

if query_string == None:
    print(html)
elif query_string == '':
    print(html)
elif int(data['answer'][0]) == quest_data['right']:
    html = html.replace('<!--#result-->', f'{int(data['answer'][0])} is correct answer!')
    print(html)
else:
    html = html.replace('<!--#result-->', f'{int(data['answer'][0])} is wrong, think further!')
    html = html.replace('res', 'res-2')
    print(html)
