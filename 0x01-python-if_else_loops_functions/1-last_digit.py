#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mod_num = number % 10 if number >= 0 else ((-number % 10) * -1)
msg = f"Last digit of {number} is {mod_num}"
if mod > 5:
    print(f"{mgs}and is greater than 5")
elif mod == 0:
    print(f"{msg}and is 0")

else:
    print(f"{msg} and is less than 6 and not 0")
