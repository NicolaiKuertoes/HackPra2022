#!/usr/bin/env python3

with open('output.txt', 'r') as filp:
    output = filp.read()[:-1].split('\n')

# f.write(iv.hex() + aes1.encrypt(aes2.encrypt(flag)).hex() + "\n")

aes_iv      = output[0][:32]
flag_enc    = output[0][32:]
png_sig_enc = flag_enc[:16]
key1_frag   = output[1]
key2_frag   = output[2]
png_sig     = "89504E470D0A1A0A"

def generate_key(key_frag, n):
    keys = set()
    key = bytearray(bytes.fromhex(key_frag + "000000"))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                key[13] = i
                key[14] = j
                key[15] = k
                keys.add(key)
    return keys

print(generate_key(key1_frag, 1))

