#!/usr/bin/python3

for i in range(100):
    if i < 99:
        print("{:02d},".format(i), end=" ")
    else:
        print("{} ".format(i), end="")


# for n in range(0, 100):
#     if n != 99:
#         print('{:02d},'.format(n), end=' ')
#     else:
#         print('{:02d}'.format(n))
