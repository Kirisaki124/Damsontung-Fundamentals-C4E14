# from random import *
# def add(x, y):      # no agrument
#     print(x + y)

def evaluate(x, y, op):
    if op == "+":
        res = x + y
    elif op == "-":
        res = x - y
    elif op == "*":
        res = x * y
    else:
        res = x / y
    return res

# print(__name__)
