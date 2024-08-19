import socket

def sendfile(path):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 12345))
        print("Connected to the server")

        with open(path, 'r', encoding='utf-8') as f:
            txt = f.read()

        s.sendall(txt.encode('utf-8'))
        print("File content sent to the server")

        s.shutdown(socket.SHUT_WR)

        cnt = int(s.recv(1024).decode('utf-8'))
        print(f"Word count: {cnt}")

    finally:
        s.close()

sendfile('example.txt')