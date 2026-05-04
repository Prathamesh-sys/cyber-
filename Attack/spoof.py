from scapy.all import *

fake_ip = "192.168.5.133"
target_ip = "127.0.0.1"

for i in range(5):
    packet = IP(src=fake_ip, dst=target_ip) / TCP(dport=80) / "Hello"
    
    print(f"\nSending Packet {i+1}")
    packet.show()   # shows full packet structure
    
    send(packet, verbose=0)