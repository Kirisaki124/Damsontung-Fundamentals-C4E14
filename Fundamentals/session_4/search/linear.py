num = [1, 2, 3, 4, 5, 6, 7, 8]

for i in range(len(num)):
    gues = int(input("Number: "))
    if gues == num[i]:
        print("found in index", num[i])
        break
    else:
        print("not found")
