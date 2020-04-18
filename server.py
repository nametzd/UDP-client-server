import socket
import operator
import sys
import binascii
import struct

def crc32(v):
    return binascii.crc32(v.encode())

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 1999))
print("Waiting...")
a = []
while True:
    data, addr = s.recvfrom(1024)
    str,crc = struct.unpack("!50sL",data)
    str = str.decode("utf-8").replace("\0","")
    print("str:%s\ncrc:%X" % (str,crc & 0xffffffff))
    a.append(str)
    if len(a) == 2:
        if a[0] != a[1]:
            print("the string has changed")
        a.clear()

    if str == "bye":
        break
