# Import socket module
from socket import * 
import sys # In order to terminate the program

serverName = 'localhost'
# Assign a port number
serverPort = 1200

# Bind the socket to server address and server port
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))

print('1-connect')
print('2-disconnect')
print('3-POST')
print('4-GET')
print('5-PIN')
print('6-UNPIN')
print('7-exit')

connectionEstablished = False

input1 = input('Input: ')

while input1 != 7:
		
	
	if input1 == '3':
		clientSocket.send(input1.encode())
		output = clientSocket.recv(1024)

		input2 = input('POST ')

		commandInput = 'POST'
		splitInput = input2.split()
		lower_left = splitInput[0]
		upper_right = splitInput[1]
		width = splitInput[2]
		height = splitInput[3]
		color = splitInput[4]
		message = splitInput[5:]
		
		# clientSocket.send(input2.encode())

		s = ' '
		joinedMessage = s.join(message)
		
		print(lower_left)
		print(upper_right)
		print(width)
		print(height)
		print(color)
		print(joinedMessage)

		a = [lower_left, upper_right, width, height, color, joinedMessage]
		clientSocket.send(commandInput.encode())

		input1 = 0



	elif input1 == '4':
		input2 = input('GET ')
		clientSocket.send(input1.encode())
		output = clientSocket.recv(1024)

	elif input1 == '5':
		input2 = input('PIN')
		clientSocket.send(input1.encode())
		output = clientSocket.recv(1024)

	elif input1 == '6':
		input2 = input('UNPIN')
		clientSocket.send(input1.encode())
		output = clientSocket.recv(1024)

	elif input1 == '1':
		print('...Connecting to server...')
		clientSocket.send(input1.encode())
		output = clientSocket.recv(1024)

	elif input1 == '2':
		print('...Disconnecting from server...')
		clientSocket.close()

	elif input1 == '7':
		print('...Exiting program...')
		output = clientSocket.recv(1024)
		break
	
	input1 = input('Input: ')
	

print(input1)


print('From server:', output.decode())
clientSocket.close()