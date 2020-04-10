import socket
import threading

class Client:
	host = input(str("Please enter hostname of server:"))
	port = 2606
	def __init__(self,host,port):
		self.host = host
		self.port = port
		self.s = socket.socket()
		self.s.connect((host, port))
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
