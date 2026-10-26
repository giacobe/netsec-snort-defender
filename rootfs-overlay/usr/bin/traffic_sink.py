#!/usr/bin/env python3
"""Small TCP listeners that make generated HTTP conversations established."""
import socket, threading, time
def serve(port):
    sock=socket.socket(); sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1); sock.bind(("0.0.0.0",port)); sock.listen(8)
    while True:
        connection,_=sock.accept()
        try:
            connection.settimeout(1); connection.recv(4096)
            connection.sendall(b"HTTP/1.1 200 OK\r\nContent-Length: 2\r\nConnection: close\r\n\r\nOK")
        except OSError: pass
        finally: connection.close()
for value in (80,84,8080): threading.Thread(target=serve,args=(value,),daemon=True).start()
while True: time.sleep(3600)
