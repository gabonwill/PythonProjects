#Server.py

import socket

class Server():

	def __init__(self):

		#reserve a port 
		self.port = 8080
		#create socket object
		self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def create():
		
		print "Socket successfully created"
		
		#bind to the port
		self.serversocket.bind(('127.0.0.1', 8080))
		print "socket binded to %s " %8080
		#put the socket into listening mode
		self.serversocket.listen(8080)
		print "listening on socket"
		#a forever loop until we interrupt it or an error occurs
		while True:
			#client connection established
			client, addr = serversocket.accept()
			data = client.recv(4096)
			print 'Got connection from', addr


	def send(self, message):
		# send a thank you message to client
		if data:
			client.send("Thank you for connecting")


	create()
	send()

	client = Server()

	
	client.send()

	#close connection with client
	client.close()