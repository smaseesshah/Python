# from telnetlib import IP
# from scapy.all import *
# import os

# a = sniff(count=10)  # type: ignore

# # Ensure the directory exists
# os.makedirs('practice', exist_ok=True)

# with open('practice/9_scapy.txt', 'a', encoding='utf-8') as f:
#     for i in range(10):
#         a[i].show()
#         f.write(str(a[i].show))
#         f.write('\n')
#new_pack = IP(dst ="www.uop.edu.pk")
#print(new_pack.show())
# new_pack = Ether()/IP(dst = "uop.edu.pk")/ ICMP()/"Cisco Academy"
# new_pack.show()
# print(new_pack.summary())
# srp(new_pack)
# ans,unans = srp(new_pack)
# new_pack2 = IP(ttl=10)
# new_pack2.src = "8.8.8.8"
# new_pack2.dst = "121.52.147.18"
# print(new_pack2.show())
# # del(new_pack2.ttl) #will be default again
# new_pack3 = Ether()/new_pack2/ICMP()/"lets hack the world"
# new_pack3.show()
# srp(new_pack3)
# udp_pack = Ether()/IP(dst="192.168.0.117",src="192.168.0.109")/UDP(dport=53,sport=50000)/"i love you"
# srp(udp_pack)

from scapy.all import *

# Define the file path
file_path = 'practice/9_scapy.py'

# Read the file contents
with open(file_path, 'rb') as file:
    file_data = file.read()

# Construct the packet with the file contents as payload
tcp_pack = Ether()/IP(src="192.168.0.115",dst="192.168.0.116")/UDP(dport=80, sport=50000)/Raw(load=file_data)

# Send the packet
sendp(tcp_pack)