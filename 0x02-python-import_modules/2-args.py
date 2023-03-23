#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)-1
    if length == 0:
        print("{} arguments.".format(length))
    elif length == 1:
        print("{} argument:".format(length))
        print("{}: {}".format(length, argv[length]))
    else:
        print("{} arguments:".format(length))
        for num in range(1, len(argv)):
            print("{}: {}".format(num, argv[num]))
