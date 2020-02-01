import socket, threading
import sys


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

	
	
# Declaring board parameters
boardWidth = sys.argv[2]
boardHeight = sys.argv[3]
colours = []
noteList = []


# Fill colours array with colour values from argv
i = 4
while i < (len(sys.argv)):
    	
	colours.append(sys.argv[i])

	i+=1
	
print('BOARD WIDTH' + boardWidth)
print('BOARD HEIGHT' + boardHeight)


class ClientThread(threading.Thread):
	def __init__(self,clientAddress,clientsocket):
		threading.Thread.__init__(self)
		self.csocket = clientsocket
		print ("New connection added: ", clientAddress)
	def run(self):
		print ("Connection from : ", clientAddress)
		commandInput = 0
		
		
		
		#self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
		msg = ''
		while True:
			print('TESTING 0')
			
			splitMsg =msg.split()
			
			if len(splitMsg) > 0:
				commandInput = splitMsg[0]
			
			data = self.csocket.recv(2048)
			msg = data.decode()
			
			if msg == '1':
				break
			
			if msg=='2':
				
				break
			print(splitMsg)
			
			if commandInput == 'POST':
				
				
				
				if len(splitMsg) >= 6:
					
					
					
					x = splitMsg[1]
					y = splitMsg[2]
					width = splitMsg[3]
					height = splitMsg[4]
					colour = splitMsg[5]
					message = splitMsg[6:]
					
					s = ' '
					joinedMessage = s.join(message)
					
					print('X ' + x)
					print('Y ' + y)
					
					if (colour in colours) and (int(x) + int(width) < int(boardWidth)) and (int(y) + int(height) < int(boardWidth)):
						
						note = Note(x, y, width, height, colour, joinedMessage, 0)
						noteList.append(note)
						msg = 'NOTE POSTED'
    					

					else:
    						
						msg = 'NOTE NOT POSTED'

				else:
    				
					msg = 'NOTE NOT POSTED'


			if commandInput == 'GET':
				print('GET')

			if commandInput == 'PIN':
				
				if len(splitMsg) == 3:
					
					x = splitMsg[1]
					y = splitMsg[2]
					
					for i in range(len(noteList)):
						noteList[i].pins += 1

					msg = 'PINNED'
				msg = 'NOT PINNED'
			
			if commandInput == 'UNPIN':
				
				if len(splitMsg) == 3:
					
					x = splitMsg[1]
					y = splitMsg[2]

					for i in range(len(noteList)):
							
						if noteList[i].pins >0:
								
							noteList[i].pins -= 1

			print ("from client", msg)
			
			
			self.csocket.send(bytes(msg,'UTF-8'))
			commandInput = ''
			x = ''
			y = ''
			width = ''
			height = ''
			colour = ''
			message = ''
			


		print ("Client at ", clientAddress , " disconnected...")
		
LOCALHOST = "127.0.0.1"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("...Waiting for client request..")



while True:
	server.listen(1)
	clientsock, clientAddress = server.accept()
	newthread = ClientThread(clientAddress, clientsock)
	newthread.start()
