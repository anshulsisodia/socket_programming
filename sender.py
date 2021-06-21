from os import scandir
import socket
import time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
recvr_addr=('3.235.20.173',9999)
while 3 > 1:
    user_data= input("enter your message-")
    new_data=user_data.encode('ascii')
    s.sendto (new_data,recvr_addr)
    time.sleep(2)
    print('your message has been sent...')