#!/usr/bin/env python3
from Crypto.Cipher import AES

# TCP_Hex_Stream from pcap
with open('tcp_hex_dump.txt', 'r') as f:
    dump = f.read()

# AES-Key from CCC-Analysis (page 4)
key = bytes.fromhex("""
49 03 93 08 19 94 96 94   28 93 83 04 68 28 A8 F5
0A B9 94 02 45 81 93 1F   BC D7 F3 AD 93 F5 32 93
""")

# Create new AES-ECB cipher with the above key
cipher = AES.new(key, AES.MODE_ECB)
# Decrypt complete TCP_Hex_Stream
out = cipher.decrypt(bytes.fromhex(dump))

# 16 Byte header (see CCC analysis page 7)
len_header = 32

# Number of bytes that should be read (see CCC analysis page 10)
jpg_size = int(out.hex()[len_header:len_header+8], 16)

# Write decrypted JPG file to disk
with open('flag.jpg', 'wb') as f:
    f.write(out[len_header:len_header+jpg_size])

print(0)
exit()
