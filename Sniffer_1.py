#to capture IP packets one time when the socket is bound to a network interface
import socket
host = socket.gethostbyname(socket.gethostname())
print("host: ", host)
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
s.bind((host, 0))
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
ipHeader = s.recvfrom(65565)
print("Packet Header: ", ipHeader)
tcpData = s.recvfrom(65565)
print("Packet Data: ", tcpData)


