#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

    length = len(argv)-1
    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:

        operator = argv[2]
        if operator != '+' and operator != '-' and \
                operator != '*' and operator != '/':
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        from calculator_1 import add, mul, sub, div
        a = int(argv[1])
        b = int(argv[3])
        if operator == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif operator == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif operator == '/':
            print("{} / {} = {}".format(a, b, div(a, b)))
        elif operator == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
