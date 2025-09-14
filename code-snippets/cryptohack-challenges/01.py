#!/usr/bin/env python3

import sys
import base64
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

ords = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

print("Here is your flag:")


print("".join(chr(o) for o in ords))

hexStr = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

bytes = bytes.fromhex(hexStr)
print(bytes)
print(list(bytes))
result = base64.b64encode(bytes)
print(result)
