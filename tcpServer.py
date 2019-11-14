#tcpServer
import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 31337

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))

server.listen(5)
print("[*] Listening on: ", bind_ip, bind_port)

#this is our client-handling thread
def handle_client(client_socket):
	#print out what client sends

	request = client_socket.recv(1024)
	print("[*] Received: ", request)

	#send back a packet
	client_socket.send("Are you ready to hack?".encode())	
	client_socket.close()

while True:
	client, addr = server.accept()
	print("[*] Accepted connection from:",  addr[0],addr[1])
	#spin up our thread to handle incoming data
	client_handler = threading.Thread(target = handle_client, args = (client,))
	client_handler.start()



