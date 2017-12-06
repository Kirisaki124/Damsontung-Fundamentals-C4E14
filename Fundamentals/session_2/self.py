from turtle import *

n = int(input("numbers"))

for i in range(n-1):

    if i%3 == 0:
        color("blue")
    else:
        color("red")
    forward(100)
mainloop()
