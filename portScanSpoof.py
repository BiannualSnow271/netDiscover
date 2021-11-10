from scapy.all import *

Ipsource = "10.0.1.1"
Ipdestiny = "10.0.1.2"
srcPort = 4000
portsScan=[20,21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1723,3306,3389,5000,5900,8000,8080]
for port in portsScan:
    spoofed_packet = sr1(IP(src=Ipsource, dst=Ipdestiny)/ TCP(sport=srcPort,dport=port),iface="tun0", timeout=5)
