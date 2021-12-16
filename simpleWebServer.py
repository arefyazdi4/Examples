from socket import *


def create_server():
    # crating an end point like waiting 4 phone call
    server_socket = socket(AF_INET, SOCK_STREAM)
    try:
        # it's like connect in browser but in here it says this is my phone number
        server_socket.bind(('localhost', 9000))
        # max number phone call that can be hold, queue until sever be be free
        server_socket.listen(5)
        while 1:
            # blocking(next line doesn't execute), it wait until phone call came in it can wait 4 ever
            (client_socket, address) = server_socket.accept()

            rd = client_socket.recv(5000).decode()
            pieces = rd.split("\n")
            if len(pieces) > 0:
                print(pieces[0])

            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"
            client_socket.sendall(data.encode())
            client_socket.shutdown(SHUT_WR)
    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as exc:
        print("Error:\n")
        print(exc)

    server_socket.close()


if __name__ == '__main__':
    print("Access http://localhost:9000")
    create_server()
