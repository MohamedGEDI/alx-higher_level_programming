#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    n = len(sys.argv)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if n != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
    else:
        if sys.argv[2] == '+':
            print("{} {} {} = {}".format(a, sys.argv[2], b, add(a, b)))
        elif sys.argv[2] == '-':
            print("{} {} {} = {}".format(a, sys.argv[2], b, sub(a, b)))
        elif sys.argv[2] == '*':
            print("{} {} {} = {}".format(a, sys.argv[2], b, mul(a, b)))
        elif sys.argv[2] == '/':
            print("{} {} {} = {}".format(a, sys.argv[2], b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
