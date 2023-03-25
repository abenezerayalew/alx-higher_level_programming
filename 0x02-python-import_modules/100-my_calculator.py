#!/usr/bin/python3
from sys import argv
from calculator_1 import add, mul, sub, div
length = len(argv)-1
if length != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
else:
    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]
    if operator == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif operator == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif operator == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
    elif operator =='*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)