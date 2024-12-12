# -------------------  python-socket-programming-server-client --------------------------

"""
Приклад:
https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client
Документація для socket:
https://realpython.com/python-sockets/
"""
import random
import socket
from dao import *

def choose_answer(data):
    rows = get_answer_by_question(data.lower())
    if len(rows) == 0:
        return choose_answer("")
    row = random.choice(rows)
    return row[0]


def server_program():

    host = socket.gethostname()             # отримати ім'я хоста
    port = 5001                            # ініціювати порт вище за 1024 - харткодовою константою

    server_socket = socket.socket()         # ініціалізація екземпляру сокета
    server_socket.bind((host, port))        # зв'язати адресу хоста та порт разом

    server_socket.listen(2)                 # налаштуйте, скільки клієнтів сервер може "слухати" одночасно
    conn, address = server_socket.accept()  # прийняти нове з'єднання
    print("Connection from: " + str(address))

    init_db()

    # організація діалогу із клієнтом
    while True:
        # отримати потік даних, він не приймає блоки даних, більші за 1024 байти
        data = conn.recv(1024).decode()
        if not data:
            # якщо дані не отримані, break
            break
        print("from connected user: " + str(data))
        answer = choose_answer(str(data))
        print(answer)
        data = f'{answer}'               # введіть відповідь клієнту
        conn.send(data.encode())            # відправити відповідь клієнту

    conn.close()                            # закрийте з'єднання
    close_db()

if __name__ == '__main__':
    server_program()