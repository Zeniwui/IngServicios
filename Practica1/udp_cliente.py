from sys import argv

import socket

if len(argv) < 1:
    print("Uso: python3 udp_cliente.py host port")
    exit()

host =  argv[1]
port = int(argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
linea = ""

while linea != "FIN":
    linea = input("Ingrese un mensaje (o FIN para terminar): ")
    s.sendto(linea.encode("utf-8"), (host, port))
