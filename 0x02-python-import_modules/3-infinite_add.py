#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    new = []
    if len(argv) == 1:
        print(0)
    elif len(argv) > 1:
        argv.pop(0)
        for i in range(len(argv)):
            new.append(int(argv[i]))
        print(sum(new))
