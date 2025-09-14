from Crypto.Util.number import *

# print(bytes_to_long(b"ab"))

# print(long_to_bytes(11515195063862318899931685488813747395775516287289682636499965282714637259206269))


def xor(a, b):
  result = ""
  for o in a:
    # val = format(ord(o), 'b')
    # print(val)
    r = ord(o) ^ b
    print(r)
    result = result + chr(r)



    print(o)
  print(result)


# print(chr(111))
# xor("label", 13)

"""
KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
"""

k1_hex = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
k2_xor_k1_hex = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
k2_xor_k3_hex = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
f_k2_xor_k1_k3_k2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
key1_bytes = list(bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"))
# print(key1_bytes)

a = int("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313", 16)
res = a ^ a
# print(res)


def xor_hex(hex1: str, hex2: str) -> str:
  b1 = bytes.fromhex(hex1)
  b2 = bytes.fromhex(hex2)

  if len(b1) != len(b2):
    raise ValueError("Hex strings must be the same length")
  
  result_bytes = bytes([x ^ y for x, y in zip(b1, b2)])

  return result_bytes.hex()


k2_hex = xor_hex(k2_xor_k1_hex, k1_hex)
k3_hex = xor_hex(k2_xor_k3_hex, k2_hex)
flag = xor_hex(xor_hex(xor_hex(f_k2_xor_k1_k3_k2, k1_hex), k2_hex), k3_hex)

print(bytes.fromhex(flag))
