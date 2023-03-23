#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            num = 32
        else:
            num = 0
        print("{:c}".format(ord(str[i]) - num), end='')
    print()
# The optimized one
# def uppercase(str):
#     for letter in range(len(str)):
#         lower = ord(str[letter])-32 if ord(str[letter]) >= 97 and ord(str[letter]) <= 122 else ord(str[letter])
#         print(chr(lower),end='')
#     print()