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

class Note(object):
	message= ""
	colour = ""
	x = 0
	y=0
	height=0
	pins=0
	width=0

	# The class "constructor" - It's actually an initializer ,pin
	def __init__(self, x, y, width, height, colour, message, pins):
		self.message = message
		self.colour = colour
		self.width = width
		self.height = height
		self.x = x
		self.y = y
		self.pins=pins

	

def pin(x,y):
	print('pinning')

def unpin(x,y):
	print('unpinning')



while True:
	print('The server is ready to receive')
	
	# Set up a new connection from the client
	connectionSocket, addr = serverSocket.accept()







	
	# splitInput = input1.split()
	# lower_left = splitInput[1]
	# upper_right = splitInput[2]
	# width = splitInput[3]
	# height = splitInput[4]
	# color = splitInput[5]
	# message = splitInput[6:]
	
	# s = ' '
	# joinedMessage = s.join(message)
	# newNote = Note(lower_left, lower_right, width, height, 'pinned', color, joinedMessage)
	# if input1 == '3':
	# 	output = 'case1'
	# 	print(lower_left)
	# 	print(upper_right)
	# 	print(width)
	# 	print(height)
	# 	print('color', color)
	# 	print(joinedMessage)

	# elif input1 == '4':
	# 	output = 'case2'

	# elif input1 == '5':
	# 	output = 'case3'
	
	# elif input1 == '6':
	# 	output = 'case4'
	
	# elif input1 == '1':
	# 	output = 'case 5'
	
	# elif input1 == '2':
	# 	output = 'Disconnecting from server'
	# 	connectionSocket.send(output.encode())
	# 	connectionSocket.close()
		
	input2 = connectionSocket.recv(1024).decode()
	print(input2)

	splitInput = input2.split()
	
	commandInput = splitInput[0]

	if commandInput == 'POST':
		x = splitInput[1]
		y = splitInput[2]
		width = splitInput[3]
		height = splitInput[4]
		colour = splitInput[5]
		message = splitInput[6:]

		s = ' '
		joinedMessage = s.join(message)

		note = Note(x, y, width, height, colour, joinedMessage, 0)

	output = commandInput
	connectionSocket.send(output.encode())
	connectionSocket.close()
	

serverSocket.close()  
sys.exit()#Terminate the program after sending the corresponding data
