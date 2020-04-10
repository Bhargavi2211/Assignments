import socket
import threading

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.s = socket.socket()
        self.s.bind((host, port))
        print("Server done binding to host and port successfully")
        print("Server is waiting for connection")
        self.s.listen(2)
        self.conn, addr = self.s.accept()
        print(addr, "Has connected to server and online")
        self.t1 = threading.Thread(target=self.incoming_message)
        self.t2 = threading.Thread(target=self.send)
        self.t1.start()
        self.t1.join()
        self.t2.join()

    def incoming_message(self):
        self.t2.start()
        while True:
            message = self.conn.recv(1024).decode()
            print("Client:", message)
            if message == 'Bye Server':
                break

    def send(self):
        while True:
            message = input("")
            self.conn.send(message.encode())
            if message == "Bye Client":
                break

host = socket.gethostname()
print("Server will start on host:", host)
port = 2606

object = Server(host, port)

