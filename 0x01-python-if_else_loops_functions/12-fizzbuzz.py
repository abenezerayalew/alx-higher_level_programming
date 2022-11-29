#!/usr/bin/python3
def fizzbuzz():
    a = range(1,100)
    for i in a[i]:
        if i % 3 == 0:
            print("Fizz", end = "")
        elif i % 5 == 0:
            print("Buzz",  end = "")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz",  end = "")
        else:
            print(i)
