import socket


def client_socket():
    clt_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаём сокет (семейство адресов IPv4, тип сокета)
    clt_socket.connect(('127.0.0.1', 9090))  # устанавливаем соединение с сервером

    msg1 = input('Введите сообщение №1: ')
    msg2 = input('Введите сообщение №2: ')
    msg3 = input('Введите сообщение №3: ')

    clt_socket.send(bytes(f'{msg1}\n{msg2}\n{msg3}\n', encoding='utf-8'))  # отправляем дынные на сервер

    data = clt_socket.recv(1024)  # получаем ответ от сервера
    print(f'Сервер отправил данные: {data.decode(encoding='utf-8', errors='strict')}')

    clt_socket.send(b'shutdown')  # отправляем ключевое слово на сервер

    clt_socket.close()  # закрываем соединение


if __name__ == '__main__':
    client_socket()
