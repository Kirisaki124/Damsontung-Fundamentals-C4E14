from calc import *
from random import *

x = randint(0, 10)
y = randint(1, 10)
op = choice(["+"] * 50 + ["-"] * 25 + ["*"] * 10 + ["/"] * 15)
error = randint( -1,1)
res = evaluate(x , y , op) + error
print(x, op, y, "=",res )
ans = input("Y/N").upper()

if ans == "Y":
    if error == 0:
        print("correct")
    else:
        print("wrong")
else:
    if error != 0:
        print("correct")
    else:
        print("wrong")
