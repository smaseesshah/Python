from scapy.all import *
import getmac

target_ip = "121.52.147.18"
target_mac = getmac.get_mac_address(ip=target_ip)

with open('practice/output.txt', 'a', encoding='utf-8') as file:
    for port in range(1, 65001):
        packet = Ether()/IP(src="192.168.1.104", dst=target_ip) / TCP(dport=port, flags="S")
        response = sr1(packet, timeout=1, verbose=False)

        if response is not None:
            if response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
                result = f"Port {port} is open"
            else:
                result = f"Port {port} is closed"
        else:
            result = f"No response from port {port}"

        file.write(result + "\n")

print(f"Output saved to practice/output.txt")
print(f"Output saved to {output_file}")