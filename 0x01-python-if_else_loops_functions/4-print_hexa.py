#!/usr/bin/python3
for num in range(99):
    print("{:d} = {:s}".format(num, hex(num)))
    # The simple one
    # print(f"{num:d}  =  {num:#04x}")