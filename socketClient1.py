import socket #Imported sockets module
import sys
try:
#Create an AF_INET (IPv4), STREAM socket (TCP)
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, e:
    print 'Error occurred while creating socket. Error code: ' + str(e[0]) +' , Error message : ' + e[1]
    sys.exit()
print 'Success!'
