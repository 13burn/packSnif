"""
IMPORTANT: In linux this requires super user credentials
"""
import socket

conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

while True:
    raw_data, addr = conn.recvfrom(65536)
    print("*********************************************************************")
    print(addr)
    print(raw_data[:6].hex())

#conn.recvfrom(3)[1][-1].hex()