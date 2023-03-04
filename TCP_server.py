import socket



serv_sock = socket.socket(socket.AF_INET,      # задамем семейство протоколов 'Интернет' (INET)
                          socket.SOCK_STREAM,  # задаем тип передачи данных 'потоковый' (TCP)
                          proto=0)             # выбираем протокол 'по умолчанию' для TCP, т.е. IP

#print(type(serv_sock))                         # <class 'socket.socket'>
#print(serv_sock.fileno())  # 3 или другой int

# указываем порт и ip на котором наш веб сервер будет слушать

serv_sock.bind(('127.0.0.1', 53210))  # чтобы привязать сразу ко всем, можно использовать ''
backlog = 10  # Размер очереди входящих подключений, т.н. backlog
serv_sock.listen(backlog)

# получаем соединение из очереди 
# вызов accept() блокирующий и не будет передавать управление нашему коду до тех пор, пока кто-то
# не подключится к нашему серверу (в очереди будет хоть один)

while True:
    # Бесконечно обрабатываем входящие подключения
    client_sock, client_addr = serv_sock.accept()
    print('Connected by', client_addr)

    while True:
        # Пока клиент не отключился, читаем передаваемые
        # им данные и отправляем их обратно
        data = client_sock.recv(1024)
        if not data:
            # Клиент отключился
            break
        print(data)
        client_sock.sendall(b'I get your data, all ok - ')
        client_sock.sendall(data)

    client_sock.close()