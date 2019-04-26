#! /usr/bin/python

import socket
from multiprocessing import Process

def connect():
    s = socket.socket()
    s.connect(("10.133.1.8", 53))
    f = open("index.html")
    data = f.read(1024)
    while(data):
        s.send(data)
        data = f.read(1024)

    answer = s.recv(1024)
    print (answer)
    s.close()

while(True):
    p = Process(target=connect)
    p.start()
    p.join()
