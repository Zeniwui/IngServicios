from sys import argv

import socket

if len(argv) < 1:
    print("Uso: python3 udp_cliente.py host port")
    exit()

host =  argv[1]
port = int(argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
linea = ""

numero = 0

while linea != "FIN":
    linea = input("Ingrese un mensaje (o FIN para terminar): ")
    numero += 1
    lineas = f"{numero}: {linea}"
    s.sendto(lineas.encode("utf-8"), (host, port))

