#!/usr/bin/env python3

from random import choice
from string import ascii_uppercase
import socket, sys


# You're calling connect on the same socket you closed. You can't do that.
# As for the docs for close say:
# All future operations on the socket object will fail.
# Just move the s = socket.socket() (or whatever you have) into the loop.
# (Or, if you prefer, use create_connection instead of doing it in two steps,
# which makes this harder to get wrong, as well as meaning you don't have to guess
# at IPv4 vs. IPv6, etc.)


message = input('Press Enter to Start or "quit" to Exit -> ')
data = 'Hello'
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
    sock.send(new_data.encode())
    message = input('Press Enter to Give New Data or quit to Exit ->')
    sock.close()
    data = new_data
