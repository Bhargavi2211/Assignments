import socket
import threading

class Client:
	def __init__(self,host,port):
		self.host = host
		self.port = port
		self.s = socket.socket()
		self.s.connect((host, port))
		print("Connect to chat server")
		self.t1 = threading.Thread(target=self.incoming_message)
		self.t2 = threading.Thread(target=self.send)
		self.t1.start()
		self.t1.join()
		self.t2.join()

	def incoming_message(self):
		while True:
			message = self.s.recv(1024).decode()
			print("Server:", message)
			if message == "Bye Client":
				break

	def send(self):
		while True:
			message = input("")
			self.s.send(message.encode())
			if message == "Bye Server":
				break

host = input("Please enter hostname of server:")
port = 2606

object = Client(host, port)
