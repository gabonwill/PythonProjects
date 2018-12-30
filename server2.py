#Server.py

import socket

class Server():


	def __init__(self):
		#reserve a port 
		self.port = 8080
		#create socket object
		self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


	def create(self):
		
		print "Socket successfully created"
		#bind to the port
		self.serversocket.bind(('127.0.0.1', 8080))
		print "socket binded to %s " %8080
		#put the socket into listening mode
		self.serversocket.listen(8080)
		print "listening on socket"
		#a forever loop until we interrupt it or an error occurs
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
				break

			client.close()

server = Server()
server.create()


	#close connection with client
	#listen for ctrl c when you get a ctrl c you close
	#client.close()
	#How to store data
	#How to receive the data 
	#send data back to the client