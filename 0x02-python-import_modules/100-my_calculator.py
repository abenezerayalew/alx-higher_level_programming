#!/usr/bin/python3
from sys import argv
from calculator_1 import add, mul, sub, div
a = int(argv[1])
b = int(argv[3])
length = len(argv)
if length <= 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
else:
    operator = argv[2]
    match(operator):
        case '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
        case '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
        case '/':
            result = div(int(argv[1]), int(argv[3]))
            print("{} / {} = {}".format(a, b, div(a, b)))
        case '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
        case other:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
