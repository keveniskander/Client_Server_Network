# AUTHOR: Keven Iskander
# ID: 160634540
# COURSE: CP372

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

	def __str__(self):
		return 'x-coordinate: %s y-coordinate: %s width: %s height: %s colour: %s message: %s pins: %s' % (self.x, self.y, self.width, self.height, self.colour, self.message, self.pins)

	
	
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


class ClientThread(threading.Thread):
	def __init__(self,clientAddress,clientsocket):
		threading.Thread.__init__(self)
		self.csocket = clientsocket
		print ("New connection added: ", clientAddress)
	def run(self):
		print ("Connection from : ", clientAddress)
		commandInput = 0
		
		
		
		# self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
		msg = ''
		while True:

			try:
				data = self.csocket.recv(2048)
			except:
				print('AN ERROR OCCURED')
			msg = data.decode()
			splitMsg =msg.split()
			
			if len(splitMsg) > 0:
				commandInput = splitMsg[0]
			
			
			
			
			if msg=='2':
				msg = '...disconnecting...'
				clientsock.close()
				exit(0)
				
				
			
			
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
					
					
					
					if (colour in colours) and (int(x) + int(width) < int(boardWidth)) and (int(y) + int(height) < int(boardWidth)):
						
						note = Note(x, y, width, height, colour, joinedMessage, 0)
						noteList.append(note)
						msg = 'NOTE POSTED'
						

					else:
							
						msg = 'NOTE NOT POSTED'

				else:
					
					msg = 'NOTE NOT POSTED'
			
			

			if commandInput == 'GET':

				flag = 0
				incr = 0

				secondCommand = splitMsg[1]
				containsArray = noteList.copy()
				
				while incr < 4:
					if 'contains' in splitMsg and flag <= 2:


						try:
							containsIndex = splitMsg.index('contains')
							x = splitMsg[containsIndex + 1]
							y = splitMsg[containsIndex + 2]
							flag += 1

							for i in range(len(noteList)):

								if int(noteList[i].x) != int(x) and int(noteList[i].y != int(y)):
									containsArray.pop(i)
								
							# print('CONTAINS GET MESSAGE: ')
							
							

						except:
							print('ERROR: List index out of range')

					if ('colour' in splitMsg or 'color' in splitMsg) and flag <= 2:


						try: 
							containsIndex = splitMsg.index('colour')
							containsArray = noteList.copy()
							term = splitMsg[containsIndex + 2]
							flag += 1

							for i in range(len(noteList)):
								
								if noteList[i].colour != term:
									containsArray.pop(i)

							

						except:

							print('ERROR: term not found')
					
					if 'refersTo' in splitMsg and flag <= 2:


						try:

							containsIndex = splitMsg.index('refersTo')
							term = splitMsg[containsIndex + 2]
							flag += 1

							for i in range(len(noteList)):
								
								if term not in noteList[i].message:
									containsArray.pop(i)

						except:

							print('ERROR: term not found')

					if 'PINS' in splitMsg and flag <= 2:

						try:

							containsIndex = splitMsg.index('PINS')
							x = splitMsg[containsIndex + 1]
							y = splitMsg[containsIndex + 2]
							flag += 1

							for i in range(len(noteList)):
								
								if int(noteList[i].pins) == 0:
									containsArray.pop(i)

						except:

							print('ERROR: term not found')

					
					incr += 1

				for i in range(len(containsArray)):
								
					msg += str(containsArray[i])
					msg += ' '


			if commandInput == 'PIN':
				
				pinbool = False
				if len(splitMsg) == 3:
					
					x = splitMsg[1]
					y = splitMsg[2]

					
					for i in range(len(noteList)):
						print(noteList[i].x)
						print(noteList[i].y)
						if int(noteList[i].x) == int(x) and int(noteList[i].y) == int(y):

							noteList[i].pins += 1
							pinbool = True


					if pinbool == True:
						msg = 'PINNED'
					else:
						msg = 'NOT PINNED'
				
			
			if commandInput == 'UNPIN':
				
				unpinbool = False
				if len(splitMsg) == 3:
					
					x = splitMsg[1]
					y = splitMsg[2]

					for i in range(len(noteList)):
						
						if int(noteList[i].x) == int(x) and int(noteList[i].y) == int(y):
							
							if noteList[i].pins > 0:
								unpinbool = True
								noteList[i].pins -= 1

				if unpinbool == True:
					msg = 'UNPINNED'
				else:
					msg = 'NOT UNPINNED'

			
			
			try:
				if msg != '2':
					print ("from client", msg)
					self.csocket.send(bytes(msg,'UTF-8'))
					
			except:
				print('...closing server...')
				exit(0)


			flag = 0
			commandInput = ''
			x = ''
			y = ''
			width = ''
			height = ''
			colour = ''
			message = ''
			msg = ''
			containsArray = []
			


		print ("Client at ", clientAddress , " ...disconnected...")
		
LOCALHOST = "127.0.0.1"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("...Waiting for client request...")



while True:
	server.listen(1)
	clientsock, clientAddress = server.accept()
	newthread = ClientThread(clientAddress, clientsock)
	newthread.start()
