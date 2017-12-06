h = int(input("Input the height of the pattern: "))
w = int(input("input the wide of the pattern: "))

for i in range(h):

    for i in range(w):
        if i%2 == 0:
            print("x", end=" ")
        else:
            print("*", end=" ")
    print(" ")
