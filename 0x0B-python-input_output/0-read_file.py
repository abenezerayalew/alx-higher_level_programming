#!/usr/bin/python3
def read_file(filename=""):
    with open(filename) as file:
        lines = file.read()
    for line in lines:
        print(line, end='')