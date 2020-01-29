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

		input2 = input('POST ')
		
		input2 = 'POST ' + input2
		clientSocket.send(input2.encode())

		output = clientSocket.recv(1024)

		print('From server:', output.decode())


		input1 = 7



	elif input1 == '4':
		input2 = input('GET ')
		
		output = clientSocket.recv(1024)

	elif input1 == '5':
		input2 = input('PIN')
		
		output = clientSocket.recv(1024)

	elif input1 == '6':
		input2 = input('UNPIN')
		
		output = clientSocket.recv(1024)

	elif input1 == '1':
		print('...Connecting to server...')
		
		

	elif input1 == '2':
		print('...Disconnecting from server...')
		clientSocket.close()

	elif input1 == '7':
		print('...Exiting program...')
		clientSocket.close()
		sys.exit()
		break
	
	input1 = input('Input: ')
	

print(input1)


print('From server:', output.decode())
clientSocket.close()
