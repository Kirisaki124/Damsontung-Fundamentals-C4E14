from turtle import *

menu = ["red", "blue", "brown", "yellow", "grey"]

for i in range(5):

    color(menu[i], menu[i])

    begin_fill()
    for _ in range(4):
        forward(50)
        left(90)
    end_fill()
    penup
    forward(50)
    pendown

mainloop()
