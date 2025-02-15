import socket

c = socket.socket() # Creation of client socket
#We won't have to bind it to any that's server job it will bind socket to that port number, client will simply connect

c.connect(('localhost', 9999))#We have to mention ipaddress of the server and port number

name = input("Enter the name : ")
c.send(bytes(name, 'utf-8'))

print(c.recv(1024).decode())#WE'rer recieving, and mention the buffersize