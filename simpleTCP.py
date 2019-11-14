#simple TCP client 1
import socket

target_host = "0.0.0.0"
target_port = 31337

#create socket object

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the client
client.connect((target_host, target_port))

#send some data

client.send("GET / HTTP/1.1\r\nHost: adress.com\r\n\r\n".encode())

#recieve some data 
response = client.recv(4096)

print(response)
