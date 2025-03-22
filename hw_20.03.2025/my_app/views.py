from django.shortcuts import render
import ast
import os
import hashlib


# salt = os.urandom(2)  # сгенерируем соль
salt = 777


def index(request):
    return render(request, 'my_app/index.html')


def register(request):
    login = request.POST.get('login')
    passwd = request.POST.get('passwd')
    reg_data = {
        'login': login,
        # 'passwd': hashlib.pbkdf2_hmac('sha256', passwd.encode('utf-8'), salt, 1000)
        'passwd': str(passwd) + str(salt)
    }

    with open('my_app/files/users.dat', 'a') as file:
        file.write(str(reg_data) + '\n')
    return render(request, 'my_app/index.html')


# def valid(request):
#     if request.POST:
#         login_ch = request.POST.get('login_ch')
#         passwd_ch = request.POST.get('passwd_ch')
#         passwd_ch_h = hashlib.pbkdf2_hmac('sha256', passwd_ch.encode('utf-8'), salt, 1000)
#         with open('my_app/files/users.dat', 'r') as file:
#             file_data = []
#             for line in file:
#                 file_data.append(ast.literal_eval(line.strip()))
#             for elem in file_data:
#                 if login_ch == elem['login']:
#                     if passwd_ch_h == elem['passwd']:
#                         answer = 'Привет {}'.format(login_ch)
#                     else:
#                         answer = 'Зарегистрируйся {}'.format(login_ch)
#                 return render(request, 'my_app/login.html', context={'answer': answer})
#     return render(request, 'my_app/login.html')


def valid(request):
    if request.POST:
        login_ch = request.POST.get('login_ch')
        passwd_ch = request.POST.get('passwd_ch')
        log_data = {
            'login': login_ch,
            # 'passwd': hashlib.pbkdf2_hmac('sha256', passwd_ch.encode('utf-8'), salt, 1000)
            'passwd': str(passwd_ch) + str(salt)
        }

        with open('my_app/files/users.dat', 'r') as file:
            file_data = file.readlines()

            if str(log_data) + '\n' in file_data:
                answer = 'Привет {}'.format(login_ch)
            else:
                answer = 'Зарегистрируйся или введи верный пароль {}'.format(login_ch)

            return render(request, 'my_app/login.html', context={'answer': answer})
    return render(request, 'my_app/login.html')
