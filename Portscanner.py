import socket
import sys
import threading
import queue
import time
import os
import platform
from socket import *


# common_ports = {
#     "21": "FTP",
#     "22": "SSH",
#     "23": "Telnet",
#     "25": "SMTP",
#     "53": "DNS",
#     "80": "HTTP",
#     "194": "IRC",
#     "443": "HTTPS",
# }
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.settimeout(5)
#
# host = input("Please enter the IP you want to scan: ")
# port = int(input("Please enter the port you want to scan: "))
#
# def portscanner(port):
#     if s.connect_ex((host, port)):
#         print("The port is closed")
#     else:
#         print("The port is open")
# portscanner(port)


# startTime = time.time()
#
# if __name__ == '__main__':
#    target = input('Enter the host to be scanned: ')
#    t_IP = gethostbyname(target)
#    print ('Starting scan on host: ', t_IP)
#
#    for i in range(50, 500):
#       s = socket(AF_INET, SOCK_STREAM)
#
#       conn = s.connect_ex((t_IP, i))
#       if(conn == 0) :
#          print ('Port %d: OPEN' % (i,))
#       s.close()
# print('Time taken:', time.time() - startTime)



from datetime import datetime
net = input("Enter the Network Address: ")
net1= net.split('.')
a = '.'

net2 = net1[0] + a + net1[1] + a + net1[2] + a
st1 = int(input("Enter the Starting Number: "))
en1 = int(input("Enter the Last Number: "))
en1 = en1 + 1
oper = platform.system()

if (oper == "Windows"):
   ping1 = "ping -n 1 "
elif (oper == "Linux"):
   ping1 = "ping -c 1 "
else :
   ping1 = "ping -c 1 "
t1 = datetime.now()
print ("Scanning in Progress:")

for ip in range(st1,en1):
   addr = net2 + str(ip)
   comm = ping1 + addr
   response = os.popen(comm)

   for line in response.readlines():
      if(line.count("TTL")):
         break
      if (line.count("TTL")):
         print (addr, "--> Live")

t2 = datetime.now()
total = t2 - t1
print ("Scanning completed in: ",total)
