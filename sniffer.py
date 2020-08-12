"""
IMPORTANT: In linux this requires super user credentials
"""
import socket
import rawPack
import os

conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

while True:
    raw_data, addr = conn.recvfrom(65536)
    os.system("clear")
    print("*********************************************************************")
    data = rawPack.pack( raw_data.hex())
    print(f"{data.origin_ip} is sending data to {data.dest_ip}")

#conn.recvfrom(3)[1][-1].hex()