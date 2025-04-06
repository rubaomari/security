#!/usr/bin/python3
from scapy.all import *
import time


ID = 1000
dst_ip = "192.168.60.135"

# Fragment No. 1 (frag offset: 0, MF=1)
ip = IP(dst=dst_ip, id=ID, frag=0, flags=1)  	#More Fragments (MF) flag set
udp = UDP(sport=7070, dport=9090, chksum=0)  	#UDP header
udp.len = 8 + 24  + 24 + 5 			#Calculate total length (header + payload)
payload1 = "*EECS4482 - Final Exam*" + "\n"  	#First part of the payload
pkt1 = ip/udp/payload1

# Fragment No. 2 (frag offset: (8 + 24)/8=4, MF=1)
ip = IP(dst=dst_ip, id=ID, frag=4, flags=1)  # Last fragment, MF=0
ip.proto = 17
payload2 = "Ruba Alomari-219317143*" + "\n" # Remaining payload
pkt2 = ip/payload2


# Fragment No. 2 (frag offset: (8 + 24 + 24)/8=7, MF=0)
ip = IP(dst=dst_ip, id=ID, frag=7, flags=0)  # Last fragment, MF=0
ip.proto = 17
payload3 = "2024" + "\n" # Remaining payload
pkt3 = ip/payload3

#pkt1.show()
#pkt2.show()
#pkt3.show()

# Send the fragments
send(pkt1)
send(pkt2)
send(pkt3)

