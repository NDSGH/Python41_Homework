#!C:\Users\Dimm\AppData\Local\Programs\Python\Python312\python.exe

import os
from urllib.parse import parse_qs

print('Content-type: text/html', end='\n\n')

with open('./calc.html') as f:
    html = f.read()

query_string = os.getenv('QUERY_STRING')


def args_handler(query_str):
    data = parse_qs(query_str)
    arg1 = float(data['arg1'][0])
    op = data['op'][0]
    arg2 = float(data['arg2'][0])
    if op == '+':
        res = arg1 + arg2
    elif op == '-':
        res = arg1 - arg2
    elif op == '*':
        res = arg1 * arg2
    elif op == '/' and arg2 != 0:
        res = arg1 / arg2
    elif op == '^':
        res = pow(arg1, arg2)
    else:
        res = ''
    return str(res)


if query_string == None:
    query_string = 'arg1=1&op=add&arg2=1'
elif query_string == '':
    print(html)
else:
    args_handler(query_string)


html = html.replace('<!-- #result -->', args_handler(query_string))
print(html)
