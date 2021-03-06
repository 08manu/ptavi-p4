#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import json


class SIPRegisterHandler(socketserver.DatagramRequestHandler):

    """
    SIPRegisterHandler
    """

    dic = {}

    def handle(self):
        for informacion in self.client_address:
            print(informacion)
        self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
        Lista = self.rfile.read().decode('utf-8').split()
        Direccion = Lista[1]
        if Lista[0] == 'REGISTER':
            self.dic[Direccion] = self.client_address[0]
            if Lista[3] == '0':
                self.dic.clear()
            else:
                expires = Lista[3]
                self.dic['expires'] = expires
        print(self.dic)
        json_fich = self.register2json()

    def register2json(self):
        with open("register.json", 'w') as fichero_json:
            json.dump(self.dic, fichero_json)

if __name__ == "__main__":
    port = int(sys.argv[1])
    serv = socketserver.UDPServer(('', port), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
