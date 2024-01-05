#!/usr/bin/python3
# 100-my_calculator.py
# handles error messages

from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    ops = {"+": add, "-": sub, "*": mul, "/": div}

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, op, b = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])

    if op not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    result = ops[op](a, b)
    print("{} {} {} = {}".format(a, op, b, result))
