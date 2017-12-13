from random import *
# import time
# for i in range(20):
#     timeee = 10
#     print(countdown(timeee))

score = 0
while True:
    x = randint(0, 10)
    y = randint(0, 10)
    z = randint(-1, 2)
    ops = ("+","-","*","/")
    op = choice(ops)
    # print(op)
    if op == "+":
        print(x, "+", y, "=", x + y + z)
        ans = input("(Y/N)")
        if z == 0:
            if ans == "y":
                print("correct")
                score += 1
                print(score)
            elif ans == "n":
                print("wrong")
                break
            else:
                print("wrong input")
        if z != 0:
            if ans == "y":
                print("wrong")
                break
            elif ans == "n":
                print("correct")
                score += 1
                print(score)
            else:
                print("wrong input")
    elif op == "-":
        print(x, "-", y, "=", x - y + z)
        ans = input("(Y/N)")
        if z == 0:
            if ans == "y":
                print("correct")
                score += 1
                print(score)
            elif ans == "n":
                print("wrong")
            else:
                print("wrong input")
        if z != 0:
            if ans == "y":
                print("wrong")
            elif ans == "n":
                print("correct")
                score += 1
                print(score)
            else:
                print("wrong input")
    elif op == "*":
        print(x, "*", y, "=", x * y + z)
        ans = input("(Y/N)")
        if z == 0:
            if ans == "y":
                print("correct")
                score += 1
                print(score)
            elif ans == "n":
                print("wrong")
            else:
                print("wrong input")
        if z != 0:
            if ans == "y":
                print("wrong")
            elif ans == "n":
                print("correct")
                score += 1
                print(score)
            else:
                print("wrong input")
    else:
        print(x, "/", y, "=", x / y + z)
        ans = input("(Y/N)")
        if z == 0:
            if ans == "y":
                print("correct")
                score += 1
                print(score)
            elif ans == "n":
                print("wrong")
            else:
                print("wrong input")
        if z != 0:
            if ans == "y":
                print("wrong")
            elif ans == "n":
                print("correct")
                score += 1
                print(score)
            else:
                print("wrong input")
