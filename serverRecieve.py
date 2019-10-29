import socket
import sys

TCP_IP = '127.0.0.1'
TCP_PORT = 8888
BUFFER_SIZE = 1024
MESSAGE_TO_SERVER = 'Hello green hacker!'

try:
    # Create an AF_INET (IPv4), STREAM socket (TCP)
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, e:
    print 'Error occurred while creating socket. Error code: ' + str(e[0]) + ' , Error message : ' + e[1]
    sys.exit()


tcp_socket.bind((TCP_IP, TCP_PORT))
#Listening for incoming connections (max queued connections: 2)
tcp_socket.listen(2)
print('Listening...--->')
#Waits for incoming connection(blocking call)
connection, address = tcp_socket.accept()
print('Connected with:', address)

data = connection.recv(BUFFER_SIZE)
print 'Message from client:', data

connection.sendall('Thanks for connecting') #Response for the message from client
connection.close()

#keep server alive

while True:
    connection, address = tcp_socket.accept()
    print 'Cllient connected: ', address

    data = connection.recv(BUFFER_SIZE)
    print('Message from client: ', data)
    connection.sendall('Thanks for connecting')