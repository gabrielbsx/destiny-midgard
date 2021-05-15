from scapy.all import *

#resp = sniff()

print(sniff(count=1, filter="tcp and host 167.114.90.86 and port 8281"))