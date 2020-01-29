# Import socket module
from socket import * 
import sys # In order to terminate the program

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
serverPort = 1200

# Bind the socket to server address and server port
serverSocket.bind(("", serverPort))

# Listen to at most 1 connection at a time
serverSocket.listen(1)

print ('The server is ready to receive')

# Server should be up and running and listening to the incoming connections

class Note:
	def __init__(self, x, y, width, height, pin, color, message):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.pin = pin
		self.color
		self.message

	def getMessage(self):
		return self.message
	

def pin(x,y):
	print('pinning')

def unpin(x,y):
	print('unpinning')



while True:
	print('The server is ready to receive')
	
	# Set up a new connection from the client
	connectionSocket, addr = serverSocket.accept()



		
	input1 = connectionSocket.recv(1024).decode()
	print(input1)
	output = 'Data received'
	connectionSocket.send(output.encode())
	if input1 == '7':
		connectionSocket.close()
	

serverSocket.close()  
sys.exit()#Terminate the program after sending the corresponding data
