#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = {'+', '-', '*', '/'}
    if argv[2] not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if operator == "+":
        print("{} {} {} = {}".format(a, argv[2], b, add(a, b)))
    elif operator == "-":
        print("{} {} {} = {}".format(a, argv[2], b, sub(a, b)))
    elif operator == "*":
        print("{} {} {} = {}".format(a, argv[2], b, mul(a, b)))
    else:
        print("{} {} {} = {}".format(a, argv[2], b, div(a, b)))
