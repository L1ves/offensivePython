from scapy.all import * 
from scapy import all
#Create a DNS request Packet to 8.8.8.8
dns_packet = IP(dst="8.8.8.8")/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname="packetpub.com"))

#send packet and get the response 
dns_request = sr1(dns_packet, verbose=1)
#Print the response
print(dns_request[DNS].summary())

