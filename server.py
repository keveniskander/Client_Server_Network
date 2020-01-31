# Import socket module
from socket import * 
import sys # In order to terminate the program
from builtins import *

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
serverPort = 1200

# Bind the socket to server address and server port
serverSocket.bind(("", serverPort))

# Listen to at most 1 connection at a time
serverSocket.listen(5)

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

	

# def pin(x,y):
# 	print('pinning')
# 
# def unpin(x,y):
# 	print('unpinning')






# Declaring board parameters
boardWidth = sys.argv[2]
boardHeight = sys.argv[3]
colours = []
noteList = []

# def checkColour(colours, colour):
# 	count = 0
# 	for i in range(len(colours)):
# 		if colours[i]==colour:
# 			count+=1
# 	
# 	print(count)

i = 4
while i < (len(sys.argv) - 1):
	colours.append(sys.argv[i])
	i+=1


while True:
	print('The server is ready to receive')
	
	# Set up a new connection from the client
	connectionSocket, addr = serverSocket.accept()

	

	input2 = connectionSocket.recv(1024).decode()
	print(input2)

	splitInput = input2.split()
	if len(splitInput)>0:
		commandInput = splitInput[0]
		
	
	if input2 == 'EXIT':
		print('lmao1')
		output = '...Sys Exit...'
		sys.exit()
		
	elif commandInput == 'connect':
		print('connecting')
		output = 'connecting'
		

	elif commandInput == 'disconnect':
		print('disconnect')
		output = 'disconnecting'
		

	elif commandInput == 'POST':
		x = splitInput[1]
		y = splitInput[2]
		width = splitInput[3]
		height = splitInput[4]
		colour = splitInput[5]
		message = splitInput[6:]

		s = ' '
		joinedMessage = s.join(message)
		
		if (colour in colours):
		
			note = Note(x, y, width, height, colour, joinedMessage, 0)
			noteList.append(note)
			output = 'commandInput'
		else:
			output = 'ERROR: The note was not added since ' + colour + ' is not a valid colour'
		

	elif commandInput == 'GET':
		
		type = spitInput[1]
		operant = splitInput[2]
		name = splitInput[3]
		
		
		print('lol')
		
	
	elif commandInput == 'PIN':
		
		x = splitInput[1]
		y = splitInput[2]
		pinned = False
		
		for i in range(len(noteList)):
			if noteList[i].x == x and noteList[i].y == y:
				pinned = True
				noteList[i].pins += 1 
		  
		if pinned == True:
			output = 'PIN success'
		else:
			output = 'PIN failed'
			
		
	
	elif commandInput == 'UNPIN':
		
		x = splitInput[1]
		y = splitInput[2]
		unpinned = False
		
		for i in range(len(noteList)):
			if noteList[i].x == x and noteList[i].y == y:
				unpinned = True
				noteList[i].pins -= 1
				
		if unpinned == True:
			output = 'UNPIN failed'
		else:
			output = 'UNPIN sucess'
		connectionSocket.send(output.encode())
	
	print(output)
	connectionSocket.send(output.encode())
	connectionSocket.close()
	

serverSocket.close()  
sys.exit() #Terminate the program after sending the corresponding data	
