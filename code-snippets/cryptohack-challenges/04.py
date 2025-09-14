import re
import pwn
hex_val = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

bytes_val = bytes.fromhex(hex_val)

known = bytes("crypto{", "utf8")

# key = bytes([c ^ k for c, k in zip(bytes_val, known)])

key = bytes("myXORkey", 'utf8')
print("recovered key: ", key)


full_key = (key * (len(bytes_val) // len(key) + 1))[:len(bytes_val)]

print(len(bytes_val))
print(len(full_key))

print(full_key)

plain = bytes([c ^ k for c, k in zip(bytes_val, full_key)])


# flag = pwn.xor(key, bytes_val)
# print(flag.decode()
# )
print(plain.decode())
