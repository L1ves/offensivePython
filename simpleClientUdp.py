#simple client udp
import socket

target_host = "127.0.0.1"
target_port = 80

#create a cocket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send some data
client.sendto("Hello Hacker".encode(), (target_host, target_port))
#recieve some data

data, addr = client.recvfrom(4096)

print(data)

