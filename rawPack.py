import struct
import re

class pack:
    def __init__(self, data):
        self.origin_mac = self.mac_format(data[:12])
        self.dest_mac = self.mac_format(data[12:24])
        self.origin_ip = self.ip_format(data[52:60])
        self.dest_ip = self.ip_format(data[60:68])


    def mac_format(self, data):
        mac_arr = re.findall("..", data) 
        return ":".join(mac_arr)


    def ip_format(self, data):
        ip_arr = re.findall("..", data)
        ip2 = []
        for item in ip_arr:
            ip2.append( str(int(item, 16)))
        return ".".join(ip2)
