#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print("1")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operators = ["+", "-", "*", "/"]
    operator = sys.argv[2]
    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        print("1")
        exit(1)
    if operator == operators[0]:
        print("{} {} {} = {}".format(a, operator, b, add(a, b)))
    elif operator == operators[1]:
        print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
    elif operator == operators[2]:
        print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
    else:
        print("{} {} {} = {}".format(a, operator, b, div(a, b)))
