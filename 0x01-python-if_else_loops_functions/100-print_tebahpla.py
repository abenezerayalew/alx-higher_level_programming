#!/usr/bin/python3
for ch in reversed(range(97, 123)):
    print("{:c}".format(ch if (ch % 2 == 0) else (ch - 32)), end='')
# The simple one
# for letter in range(26):
#     upper = ord('Z')-letter
#     lower = ord('z')-letter
#     collection = chr(lower) if lower % 2 == 0 else  chr(upper)
#     print(collection,end='')