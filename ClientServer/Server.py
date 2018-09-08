#Потоковый TCP сокет.
import socket, time
from random import choice, randint
from string import ascii_uppercase


def main():
    pass


#By default we have socket.AF_INET, socket.SOCK_STREAM
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname(socket.gethostname())
port = 9090

print("IP Host Address:", host)
print("Port:", port)

try:
    #Теперь свяжем наш сокет с данными хостом и портом с помощью метода bind, которому передается кортеж
    sock.bind((host, port))
except socket.error as error:
    print(str(error))
# queue up to 3 requests
sock.listen(3)
# Бесконечный цикл работы программы
while True:

    # Если мы захотели выйти из программы
    question = input('Do you want to quit? y\\n: ')
    if question == 'y':
        break

    print('wait connection...')

    # accept - принимает запрос и устанавливает соединение, (по умолчанию работает в блокирующем режиме)
    # устанавливает новый сокет соединения в переменную conn и адрес клиента в переменную addr
    (conn, addr) = sock.accept()
    print('client addr: ', addr)

    error_num = 0
    # recv - получает сообщение TCP
    data = conn.recv(1024).decode()
    # если ничего не прислали, завершим программу
    if not data:
        conn.close()
        break
    else:
        print(data)
        replace = ''.join(choice(ascii_uppercase) for i in range(2))
        data_replace = data.replace(data[0:2], replace)
        for item in data:
                if not item in data_replace:
                    error_num += 1
                    print(item)

        Res = [x for x in data if not x in data_replace]
        print('Data Replace:', data_replace)
        print('Results:', Res)
        print("Error Num:", error_num)
        error_accuracy = (error_num / len(data)) * 100
        print('Error Accuracy:', error_accuracy, '%')
        print('Encode Message:', data_replace.encode())
        # send - передает сообщение TCP
        conn.send(data_replace.encode())
        #conn.send(str(error_accuracy).encode())
        # close - закрывает сокет
        conn.close()

sock.close()


if __name__ == '__main__':
    main()

# #С помощью метода listen мы запустим для данного сокета режим прослушивания. Метод принимает один аргумент — максимальное количество подключений в очереди
# sock.listen(2)
# #мы можем принять подключение с помощью метода accept
# conn, addr = sock.accept()
#
#
# print('Server Started and Listening')
# itsatime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# print("[" + itsatime + "]")
#
#
# data = conn.recv(1024)
# if not data:
#     break
# data_replace = data.replace(data[0:2], x)
# print('Original:', list(data))
# print('Replace: ', list(data_replace))
#




# while True:
#     print("Connection found!")
#     #Чтобы получить данные нужно воспользоваться методом recv, который в качестве аргумента принимает
#     # количество байт для чтения. Мы будем читать порциями по 1024 байт (или 1 кб
#     data = conn.recv(1024).decode()
#     if not data:
#         break
#     data_replace, correctNumber = manipulation_with_str(data=data)
#     print("Количество изменений:", ((correctNumber) / len(data) * 100), '%')
#     print('Server side', data)
#     conn.send(data_replace.encode())
#
# conn.close()
