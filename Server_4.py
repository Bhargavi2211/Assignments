import socket
import threading

class Server:
    host = socket.gethostname()
    print("Server will start on host:", host)
    port = 2606

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.s = socket.socket()
        self.s.bind((host, port))
        self.s.listen(2)
        self.conn, addr = self.s.accept()
        print("Connection from:", addr[0], addr[1])
        self.t1 = threading.Thread(target=self.incoming_message)
        self.t2 = threading.Thread(target=self.send)
        self.t1.start()
        self.t1.join()
        self.t2.join()

    def incoming_message(self):
        self.t2.start()
        while True:
            message = self.conn.recv(1024).decode()

            if message == 'Bye Server':
                break

    def send(self):
        while True:
            message = input("")
            self.conn.send(message.encode())
            if message == "Bye Client":
                break
