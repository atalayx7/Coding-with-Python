import socket


def main():
    host = '127.0.0.1'
    port = 502
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET: DNS'deki 4 protoküllü kısım.
    # SOCK_STREAM: Kayıpsız, statik veri yollama.
    s.bind((host, port))  # Host ve Port'u eşleştirir
    s.listen(1)  # En fazla bağlanacak kişi sayısı. 0 olursa sınırsız.

    print("Listening...: " + host)
    c, addr = s.accept()  # sunucuyu etkin hale getiriyoruz.
    print("Connection from: " + str(addr))

    while (True):
        data = c.recv(1024).decode('utf-8')  # Sunucuya bağlanmak isteyenin ismini değişkene atıyoruz.
        if not data:
            break
        print('From connected user: ' + data)
        data = data.upper()
        print('Sending: ' + data)
        c.send(data.encode('utf-8'))
    c.close()


if __name__ == '__main__':
    main()
