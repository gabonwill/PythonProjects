import socket
import datetime
import sys
import threading
import traceback
import time
import SocketServer

class Server():


	def __init__(self):
		#reserve a port 
		self.port = 53
		#create socket object
		self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	def create(self):
		
		print "Socket successfully created"
		#bind to the port
		self.serversocket.bind(('', 53))
		print "socket binded to %s " %53
		#put the socket into listening mode
		self.serversocket.listen(53)
		print "listening on socket"
		#a forever loop until we interrupt it or an error occurs

	def tcpaccept(self):
		while True:
			try:
				#client connection established
				client, addr = self.serversocket.accept()
				data = client.recv(4096)
				print 'Got connection from', addr
			
				if data:
					client.send("Thank you for connecting")
			except KeyboardInterrupt:
				client.send("Thank you for connecting")
				

	def udpaccept(self):
		while True:
			try:
				client, addr = self.serversocket.accept()
				data = client.recv(512)
				print "data"
			except KeyboardInterrupt:
				


#client.close()

#server = Server()
#server.create()


	#close connection with client
	#listen for ctrl c when you get a ctrl c you close
	#client.close()
	#How to store data
	#How to receive the data 
	#send data back to the client