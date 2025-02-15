import socket #Import the socket to use it

s = socket.socket() #Creation of the socket this takes ipv4 by default & tcp as protocol by default
print("Socket created")

#Since we're creating a server it should listens for connections to bind to 
s.bind(('localhost', 9999)) #It accepts ip address and port range 0 -> 65535 as one object

s.listen(3) #It takes no of clients for connection
print('Waiting for connections')

#Once we're listening we are waiting for connections to run in continous manner
while True:
    c, address = s.accept() #This returns client's socket and address & is responsible for accepting connections
    name = c.recv(1024).decode()
    print(f"Connected with {name}, at {address}.")

    #Sending something to client side
    c.send(bytes("Welcome at localhost", 'utf-8')) #It takes a bytes like object in a format 

    c.close() #Always close the resources
