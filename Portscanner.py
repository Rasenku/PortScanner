import socket
import sys
import threading
import queue
import time
import os
import platform
from scapy.all import *
import netaddr



common_ports = {
    "21": "FTP",
    "22": "SSH",
    "23": "Telnet",
    "25": "SMTP",
    "53": "DNS",
    "80": "HTTP",
    "194": "IRC",
    "443": "HTTPS",
}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("Please enter the IP you want to scan: ")
port = int(input("Please enter the port you want to scan: "))

def portscanner(port):
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The port is open")
portscanner(port)


startTime = time.time()

if __name__ == '__main__':
   target = input('Enter the host to be scanned: ')
   t_IP = gethostbyname(target)
   print ('Starting scan on host: ', t_IP)

   for i in range(50, 500):
      s = socket(AF_INET, SOCK_STREAM)

      conn = s.connect_ex((t_IP, i))
      if(conn == 0) :
         print ('Port %d: OPEN' % (i,))
      s.close()
print('Time taken:', time.time() - startTime)
