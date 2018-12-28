#Server.py

import socket

class Server():

	def create():
		#create socket object
		serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print "Socket successfully created"
		#reserve a port 
		port = 8080
		#bind to the port
		serversocket.bind(('127.0.0.1', 8080))
		print "socket binded to %s " %8080
		#put the socket into listening mode
		serversocket.listen(8080)
		print "listening on socket"
		#a forever loop until we interrupt it or an error occurs
		while True:
			#client connection established
			client, addr = serversocket.accept()
			print 'Got connection from', addr





	# send a thank you message to client
	client.send('Thank you for connecting')

	#close connection with client
	client.close()
