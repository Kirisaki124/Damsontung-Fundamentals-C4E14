from turtle import *

n = int(input(">3"))

shape ("turtle")



for i in range(1, n):
    forward(50)
    left(360/i)



mainloop()
