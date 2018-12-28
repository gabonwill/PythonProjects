import socket
import sys


class Client():

	def __init__(self):
		self.hostname = "127.0.0.1"
		self.port = 8080
		self.command = 'GET'
		self.filename = "index.html"
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


	def connect(self):
		try:
			self.socket.connect(("127.0.0.1", 8080))
			print "Socket successfully created"
		except:
			print "socket failed with an error"

	
	def printRecieved(self):
		print self.socket.recv(4096)
		print "the socket has successfully connected"


	def sendfunction(self):

		try:
			self.socket.sendall("GET / HTTP/1.1\r\n")
			self.socket.sendall("GET / HTTP/1.1\r\n\r\n")
		except TypeError:
			print "TypeError"
						


client = Client()
client.connect()
client.printRecieved()
client.sendfunction()

#try:
	
	#'index.html')
	#except socket.gaierror:
#except:
	#print "Error resolving host"
	#sys.exit()

#socket.connect((hostname, 8080))
#socket.sendall("GET / HTTP/1.1\r\n")
#socket.sendall("GET / HTTP/1.1\r\n\r\n")

