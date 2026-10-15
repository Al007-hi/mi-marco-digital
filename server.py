#!/usr/bin/env python3
"""Servidor local de instalación y prueba para Mi Marco. No envía fotos a Internet."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import socket, os
PORT=8000
class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control','no-cache')
        super().end_headers()
def local_ip():
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    try:
        s.connect(('192.0.2.1',80)); return s.getsockname()[0]
    except OSError: return 'IP-del-ordenador'
    finally: s.close()
if __name__=='__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print('\nMI MARCO DIGITAL - servidor de primera instalación/prueba')
    print('En el iPad abre: http://%s:%s' % (local_ip(),PORT))
    print('Mantén el ordenador y el iPad en la misma Wi-Fi. Ctrl+C para cerrar.\n')
    ThreadingHTTPServer(('0.0.0.0',PORT),Handler).serve_forever()
