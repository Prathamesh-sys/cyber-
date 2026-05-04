import argparse
from scapy.all import sniff

class Sniffer:
    def __init__(self, args):
        self.args = args

    def __call__(self, packet):
        if self.args.verbose:
            packet.show()          # Detailed output
        else:
            print(packet.summary())  # Short output

    def run(self):
        sniff(iface=self.args.interface, prn=self, store=0)

# Argument parser
parser = argparse.ArgumentParser(description="Packet Sniffer using Scapy")

parser.add_argument(
    "-v", "--verbose",
    action="store_true",
    help="Show detailed packet information"
)

parser.add_argument(
    "-i", "--interface",
    required=True,
    help="Network interface (e.g., Wi-Fi)"
)

args = parser.parse_args()

# Run sniffer
sniffer = Sniffer(args)
sniffer.run()