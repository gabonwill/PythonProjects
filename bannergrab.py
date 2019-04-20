#! /usr/bin/python

import socket

s = socket.socket()
s.connect(("10.133.1.1", 53))
answer = s.recv(1024)
print (answer)
s.close()
