import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("127.0.0.1",9999))
data_recvr=s.recvfrom(100)
print(data_recvr) 