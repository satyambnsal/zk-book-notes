
from Crypto.Util.number import *


hex_val = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
byte_val = bytes.fromhex(hex_val)
print(byte_val)
bytes_list = list(byte_val)
# print(bytes_list)

for i in range (0,256):
  print(i)
  res = []
  for v in byte_val:
    res.append(v ^ i)
  print(bytes(res))
  # print(long_to_bytes(res)) 
