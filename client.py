#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket
import sys

# Constantes. Dirección IP del servidor y contenido a enviar
if len(sys.argv) != 6:
    sys.exit("Usage: client.py ip puerto register sip_address expires_value")
server = sys.argv[1]
port = int(sys.argv[2])
expires = sys.argv[5]
registro = sys.argv[3]
metodo = "REGISTER sip:" + sys.argv[4] + " SIP/2.0\r\n\r\n" + expires

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((server, port)) 
    if registro == "register":
        print("Enviando:", metodo)
    my_socket.send(bytes(metodo, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))

print("Socket terminado.")
