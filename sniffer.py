"""
IMPORTANT: In linux this requires super user credentials
"""
import socket

conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

while True:
    print(conn.recvfrom(3))