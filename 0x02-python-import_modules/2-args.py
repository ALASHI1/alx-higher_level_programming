#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print(len(argv) - 1, "argument:")
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
    else:
        print(len(argv) - 1, "arguments:")
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
