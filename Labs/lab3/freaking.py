from random import *

x = randint(0, 10)
y = randint(0, 10)
z = randint(-1, 2)
print(x, "+", y, "=", x + y + z)
ans = input("(Y/N)")
if z == 0:
    if ans == "y":
        print("correct")
    elif ans == "n":
        print("wrong")
    else:
        print("wrong input")
if z != 0:
    if ans == "y":
        print("wrong")
    elif ans == "n":
        print("correct")
    else:
        print("wrong input")
