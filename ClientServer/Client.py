#!/usr/bin/env python3

from random import choice
from string import ascii_uppercase
import socket, sys


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname(socket.gethostname())
#порт возьмем любой от 2000 до 65535 Первая тысяча резерв систем
port = 9090
addr = (host, port)

sock.connect(addr)


#r = input('Press Enter to Start')
data = 'Hello'

#''.join(choice(ascii_uppercase) for i in range(6))
if not data :
    sock.close()
    sys.exit(1)
print('Data on Client Side:', data.encode())
sock.send(data.encode())
#sock.close()

while True:

    print('wait connection...')
    r = input('Press Enter to Give New Data')
    new_data = sock.recv(1024).decode()
    print('New Data on Client Side:', new_data)

    sock.send(new_data.encode())
    sock.close()

socket.close()


if __name__ == '__main__':
    pass