from turtle import*

menu = ["red", "blue", "brown", "yellow", "grey"]
shape("turtle")

print()
loop = 3

for i in range(5):
    color(menu[i])
    for j in range(loop):

    # col = menu[n]
    # color(menu[n])
        forward(50)
        left(360/loop)

    loop += 1

    # for j in range(4):
    #     color(menu[1])
    #     forward(50)
    #     left(360/4)

    # for i in range(5):
    #     forward(50)
    #     left(360/5)
    # color("red")
    # for i in range(6):
    #     forward(50)
    #     left(360/6)
    # em tìm thấy quy luật rồi nhưng ko biết diễn tả :))

mainloop()
