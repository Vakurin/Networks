#!/usr/bin/env python3

from random import choice
from string import ascii_uppercase
import socket, sys




#print("Enter 'quit' to exit")
#message = input(" -> ")
message = input('Press Enter to Give New Data or quit to Exit ->')
while message != 'quit':

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostbyname(socket.gethostname())
    # порт возьмем любой от 2000 до 65535 Первая тысяча резерв систем
    port = 9090
    addr = (host, port)

    try:
        sock.connect(addr)
    except:
        print('Connection error')
        sys.exit()

    data = 'Hello'
    # ''.join(choice(ascii_uppercase) for i in range(6))

    if not data:
        sock.close()
        sys.exit(1)

    print()
    print()
    print('Data on Client Side:', data)
    sock.send(data.encode())

    new_data = sock.recv(1024).decode()
    print('New Data on Client Side:', new_data)
    #message = input(" -> ")
    sock.send(new_data.encode())
    message = input('Press Enter to Give New Data or quit to Exit ->')
    sock.close()


sock.close()


