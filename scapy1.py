from scapy.all import *
from datetime import datetime
interface = 'wlan0' #interface for sniff
filter_bpf = 'udp and port 53' #BPF filter to filter udp packets in port 53

#Runs thid for each packet
def select_DNS(packet):
	packet_time = packet.sprintf('%sent.time%')
	try:
		if DNSQR in packet and packet.dport == 53:
			#Print queries
		    print 'DNS queries Message from ' + packet[ip].src  + 'to ' + packet[IP].dst + ' at ' + packet_time
		elif DNSRR in packet and packet.sport == 53:
	    	#print responses
			print 'DNS responses Message from ' + packet[IP].src + 'to ' + packet[IP].dst + ' at ' + packet_time
	except:
		pass
#Sniff the packets
sniff(iface=interface, filter=filter_bpf, store=0, prn=select_DNS)