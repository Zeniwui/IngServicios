from sys import argv

import socket
import random

if len(argv) < 1:
    print("Uso: python3 udp_servidor.py port")
    exit()

port = int(argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", port))

while True:
    datagrama, origen = s.recvfrom(1024)  # 1024 es el máximo tamaño esperado
    if (random.randint(1, 10) < 5):
        print("Simulando paquete perdido")
    else:
        print("Se ha recibido un datagrama desde", origen)
        print("Contiene lo siguiente:")
        print(datagrama.decode("utf-8"))