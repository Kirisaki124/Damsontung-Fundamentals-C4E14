from turtle import *

shape("turtle")

n = int(input("number ? "))

for i in range(n):
    color("blue","red")
    forward(50)
    penup()
    forward(50)
    pendown()
mainloop()
