#!/usr/bin/python3

for i in range(99):
    if len(str(i)) < 2:
        print("0{}, ".format(i), end="")
    else:
        print("{}, ".format(i),end="")
print(99)
