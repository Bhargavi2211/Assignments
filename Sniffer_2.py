#to capture IP packets and unpack the first byte; Got this code from a resource
import socket
import struct
host = socket.gethostbyname(socket.gethostname())
print("host: ", host)
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
s.bind((host, 0))

# Include IP headers
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# receive all packages
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# receive a packet header
ipHeader = s.recvfrom(65565)
print("Packet Header: ", ipHeader)
data = ipHeader[0]
print("*-received Data:", data)
unpackedData = struct.unpack('!BBHHHBBH4s4s', data[:20])
print("*-unpacket Data: ", unpackedData)
version_IHL = unpackedData[0]
version = version_IHL >> 4
IHL = version_IHL & 0xF
print("version: ", version)
print("IHL (Internet Header Length): ", IHL)
