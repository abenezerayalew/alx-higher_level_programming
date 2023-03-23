#!/usr/bin/python3
for number in range(100):
    if (number != 99):
        print("{}{}, ".format(int(number / 10), number % 10), end="")
    else:
        print("{}{}".format(int(number / 10), number % 10))
# The simple one
# for digit in range(100):
#     if digit != 99:
#         print("{:02d}{} ".format(digit,','),end='')
#     else:
#         print("{}".format(digit))
