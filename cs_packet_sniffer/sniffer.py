from scapy.all import *
def handler(packet):
    print(packet.summary())
    
sniff(iface="Wi-Fi", prn=handler, filter="tcp", store=0)