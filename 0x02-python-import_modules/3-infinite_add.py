#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    #num = len(sys.argv) - 1
    #if num == 0:
     #   print("{}".format(num))
        
    value = 0
    for num in sys.argv:
        if num != sys.argv[0]:
            value += int(num)
    print(value)
