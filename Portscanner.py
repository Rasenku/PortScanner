import socket
import sys
import threading
import queue
import time



common_ports = {
    "21": "FTP",
    "22": "SSH",
    "23": "Telnet",
    "25": "SMTP",
    "53": "DNS",
    "80": "HTTP",
    "194": "IRC",
    "443": "HTTPS",
    "3306": "MySQL",
    "25565": "Minecraft"
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
