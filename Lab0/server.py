import socket

def count_words(txt):
    words = txt.split()
    return len(words)

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 12345))
    s.listen()

    while True:
        client, addr = s.accept()
        print(f"Connection from {addr}")

        try:
            txt = b''
            while True:
                data = s.recv(1024)
                if not data:
                    break
                txt += data
            print("File content received")

            cnt = count_words(txt.decode('utf-8'))
            s.sendall(str(cnt).encode('utf-8'))
            print("Count sent")

        finally:
            s.close()

server()