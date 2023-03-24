#!/usr/bin/python3
from sys import argv
from calculator_1 import add, mul, sub, div
length = len(argv)
if length != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
else:
    operator = argv[2]
    match(operator):
        case '+':
            result = add(int(argv[1]),int(argv[3]))
            print("{} + {} = {}".format(argv[1],argv[3],result))
        case '-':
            result = sub(int(argv[1]),int(argv[3]))
            print("{} - {} = {}".format(argv[1],argv[3],result))
        case '/':
            result = div(int(argv[1]),int(argv[3]))
            print("{} / {} = {}".format(argv[1],argv[3],result))
        case '*':
            result = mul(int(argv[1]),int(argv[3]))
            print("{} * {} = {}".format(argv[1],argv[3],result))
        case other:
            print("Unknown operator. Available operators: +, -, * and /")


