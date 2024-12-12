# ---------------------  python-socket-programming-server-client -------------------------

"""
Приклад:
https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client
Документація для socket:
https://realpython.com/python-sockets/
"""


import socket


def client_program():

    host = socket.gethostname()                     # фіксація socket для однієї робочої станції взаємодії server-client
    port = 5001                                     # номер порту сервера сокетів - хардкодова константа

    client_socket = socket.socket()                 # ініціалізація екземпляру сокета
    client_socket.connect((host, port))             # конекція із server

    # організація діалогу із сервером
    message = input(" -> ")                         # приймання вхідних даних

    while message.lower().strip() != 'бувай':
        client_socket.send(message.encode())        # відправити повідомлення на server
        data = client_socket.recv(1024).decode()    # отримати відповідь від server

        print('Received from server: ' + data)      # відобразити відповідь у терміналі

        message = input(" -> ")                     # наступне повідомлення

    client_socket.close()                           # закрийте з'єднання


if __name__ == '__main__':
    client_program()
