print()
print("Wellcome to our shop, what you want? ")        # started
clo = ["T-shirt", "Sweater", "Jeans"]
print("Our items:", end=" ")
print(*clo, sep=", ")

loop = True
while loop:
    c = int(input("press the number: add(1), update(2), delete(3), exit(4)"))

    if c == 1:
        clo.append(input("Enter new item: "))                 #add items
        print("Our items:", end=" " )
        print(*clo, sep=", ")
    elif c == 2:
        position = int(input("Update postion: "))             #update items
        clo[position - 1] = input("Change to: ")
        print("Our items:", end=" ")
        print(*clo, sep=", ")
    elif c == 3:
        rem = int(input("Delete position:"))                 #delete items
        del clo[rem - 1]
        print("Our items:", end=", ")
        print(*clo, sep=", ")
    elif c == 4:
        break
    else:
        print("Only 1 to 4")
