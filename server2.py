# Server.py

import socket
import datetime
import sys
import threading
import traceback
import time
import SocketServer


class Server():

    def __init__(self):
        # reserve a port
        self.port = 53
        # create socket object
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def create(self):

        print "Socket successfully created"
        # bind to the port
        self.serversocket.bind(('127.0.0.1', 53))
        print "socket binded to %s " % 53
        # put the socket into listening mode
        self.serversocket.listen(53)
        print "listening on socket"
        # a forever loop until we interrupt it or an error occurs

    def run(self):

        while True:
            try:
                # client connection established
                client, addr = self.serversocket.accept()
                # data = client.recv(4096)
                print 'Got connection from', addr
                try:
                    threading.Thread(target=self.serv,
                                         args=(client, addr)).start()

                except:
                    print "Unable to start thread"
                # if data:
                #	client.send("Thank you for connecting")

            except KeyboardInterrupt:
                client.send("Thank you for connecting")
                break

        client.close()

    def serv(self,client,addr):
    	client.send('connection received')

    	client.close()


server = Server()
server.create()
server.run()

# close connection with client
# listen for ctrl c when you get a ctrl c you close
# client.close()
# How to store data
# How to receive the data
# send data back to the client
