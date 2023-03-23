#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    new_str = ""
    for ch in str:
        if i != n:
            new_str += ch
        i += 1
    return new_str
# The optimized one
# def remove_char_at(str,n):
#     str = str[:n] + str[n+1:]
#     return str