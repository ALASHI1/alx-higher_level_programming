#!/usr/bin/python3

def islower(c):
    if c.islower() and c.isalpha():
        return True
    elif c == '':
        raise ValueError('Empty string')
    else:
        return False
    

print(islower(""))