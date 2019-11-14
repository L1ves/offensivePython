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

tcp_socket.connect((TCP_IP, TCP_PORT))

try:
    #Sending message
    tcp_socket.send(MESSAGE_TO_SERVER)
except socket.error, e:
    print 'Error occurred while creating socket. Error code: ' + str(e[0]) + ' , Error message : ' + e[1]
    sys.exit()
    print 'message to the server send successfully'


