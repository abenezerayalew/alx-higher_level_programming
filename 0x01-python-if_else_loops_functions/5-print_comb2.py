#!/usr/bin/python3
for num in range(00, 100):
    if (num != 100 and num != 0):
        print(", ", end="")
    print("{:02d}".format(num), end="")
