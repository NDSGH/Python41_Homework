import socket


def server_socket():
    srv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаём сокет (семейство адресов IPv4, тип сокета)
    srv_socket.bind(('0.0.0.0', 9090))  # привязываем сокет к ip адресу и порту
    srv_socket.listen(2)  # прослушиваем входящие соединения (количество)
    print('Сервер запущен и ждёт подключений...')  # сообщение при первом запуске сервера

    while True:
        clt_socket, clt_address = srv_socket.accept()  # принимаем соединение
        print(f'Клиент подключился: {clt_address}')

        data = clt_socket.recv(1024)  # получаем данные от клиента
        print(f'Клиент отправил данные:')
        print(f'{data.decode(encoding='utf-8', errors='strict')}')

        clt_socket.send(b'data received')  # отправляем подтверждение клиенту

        sd = clt_socket.recv(1024)
        if sd.decode(encoding='utf-8', errors='strict') == 'shutdown':
            print('Клиент закрыл соединение')
            clt_socket.close()  # закрываем соединение
            break


if __name__ == '__main__':
    server_socket()
