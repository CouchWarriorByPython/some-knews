import socket
"""
Socket это пара domain:5000, через которую осуществляется
взаимодействие между двумя субъектами: клиент - сервер.
"""
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создаем субъект сервера
# AF_INET указываем поддержку IPv4, SOCK_STREAM поддержка протокола TCP
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Разрешаем повторное использование порта
server_socket.bind(('localhost', 5000))  # Привязываем наш сокет к определенному домену и порту
server_socket.listen()  # Прослушка входящего буфера на предмет каких-то подключений

"""
Так как отношения клиент-сервер длительны, то мы используем бесконечный цикл
"""
while True:
    print('Before .accept()')
    client_socker, addr = server_socket.accept()  # Вернет нам кортеж в том случае, если есть входящее соединение
    print('Connection from', addr)

    """После принятия соединения, нужно дождаться каких-то данных"""
    while True:
        request = client_socker.recv(4096)  # Принимаем сообщения, размер ограничен 4 кб

        if not request:  # Условие прерывания цикла ожидания
            break
        else:
            response = 'Hello world\n'.encode()  # Ответ в байтовом виде
            client_socker.send(response)  # Метод для отправки ответа

    print('Outside inner while loop')
    client_socker.close()  # Закрываем соединение для предотвращения ожидания