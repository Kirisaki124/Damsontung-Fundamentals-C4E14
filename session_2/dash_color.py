n = int(input("number? "))


from turtle import *
screensize(1000,1000)
pencolor("red")
shape("turtle")

for i in range(n):
    if i % 3 == 0:
        color("blue")
    else:
        color("red")
    forward(50)
    penup()
    forward(50)
    pendown()

mainloop()
