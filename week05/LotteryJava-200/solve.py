#!/usr/bin/env python3
from pwn import *
from LCG import LCG

host = "hackfest.redrocket.club" 
port = 33004

s = connect(host, port)

# Grabbing states
s.recvuntil(b"number?\n")
s.sendline(bytes("0".encode()))
states = [int(s.recvline().decode().strip().split(" ")[-1:][0])]
s.recvline()
s.sendline(bytes("0".encode()))
states.append(int(s.recvline().decode().strip().split(" ")[-1:][0]))
s.recvline().decode()

# generate prediction
l = LCG(0)

for i in range(2 ** 17):
    seed = (states[0] * (2 ** 17)) + i
    l.state = seed
    prev = l.nextInt()
    if prev == states[1]:
        s.sendline(str(l.nextInt()).encode())
        s.recvline().decode()
        print(s.recvline().decode())
        s.close()
        break
