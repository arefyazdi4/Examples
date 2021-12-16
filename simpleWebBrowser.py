import socket
# socket is like file (they way you connect with server and retrieve data

if __name__ == '__main__':
    # making a phone call its like creating start point
    my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # entering phone number
    my_sock.connect(('data.pr4e.org', 80))
    # writing a GET request and format it in UTF-8 (dont share string in internet)
    cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
    my_sock.send(cmd)

    while True:
        data = my_sock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end='')

    my_sock.close()

