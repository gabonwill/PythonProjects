import socket
import sys


class Client():

	def __init__(self):
		self.hostname = hostname
		self.port = 8080
		self.command = 'GET'
		self.filename = "index.html"

try:
	socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print "Socket successfully created"
except:
	print "socket failed with an error"

try:
	hostname = socket.gethostbyname('index.html')
except socket.gaierror:
	print "Error resolving host"
	sys.exit()

socket.connect((hostname, port))
socket.sendall("GET / HTTP/1.1\r\n")
socket.sendall("GET / HTTP/1.1\r\n\r\n")
print socket.recv(4096)
print "the socket has successfully connected"

