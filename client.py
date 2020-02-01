import socket
import sys

SERVER = "127.0.0.1"
PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
client.sendall(bytes("This is from Client",'UTF-8'))



while True:
    
    in_data =  client.recv(1024)
    print("From Server :" ,in_data.decode())
    print('1-connect')
    print('2-disconnect')
    print('3-POST')
    print('4-GET')
    print('5-PIN')
    print('6-UNPIN')
    print('7-exit')
    
    commandInput = input('Input: ')
    
    if commandInput == '3':
        
        out_data = input('POST ')
        out_data = 'POST ' + out_data
        client.sendall(bytes(out_data,'UTF-8'))
        
    
    if commandInput =='2':
       out_data = '2' 
       client.sendall(bytes(out_data,'UTF-8'))
        
    if commandInput == '1':
        out_data = '1'
        SERVER = "127.0.0.1"
        PORT = 8080
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((SERVER, PORT))
        client.sendall(bytes("This is from Client",'UTF-8'))

    if commandInput == '4':
        out_data = input('PIN ')
        out_data = 'GET ' + out_data
        client.sendall(bytes(out_data,'UTF-8'))

    if commandInput == '5':
        out_data = '5'
        out_data = 'PIN ' + out_data

        
    else:    
        client.sendall(bytes(out_data,'UTF-8'))
    
client.close()
