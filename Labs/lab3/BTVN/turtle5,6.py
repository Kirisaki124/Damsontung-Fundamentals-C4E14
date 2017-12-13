from turtle import *
# shape("turtle")
# speed(1)
def draw_star(x, y, length):
    setx(x)
    sety(y)
    for i in range(5):
        forward(length)
        right(144)


# draw_stars(0,0,100)
speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)

mainloop()
