print("*"*20)
sheep_size = [5, 7, 300, 90, 24, 50, 75]
print()
print("Hello, my name is Hiep and this is my flock")
print(sheep_size)

month = 1     # varible for loop
time = int(input("how long will you be bored of being a shepherd(month)?"))
# loop here
for i in range(time - 1):
    print("Now my biggest sheep has size", max(sheep_size), "let's shear it")
    print("After shearing, here is my flock")

    ma = sheep_size.index(max(sheep_size))
    sheep_size[ma] = 8

    print(sheep_size)
    #first end
    print()
    month += 1
    print("Month", month,":")

    print("One month has passed, now here is my flock")

    for i in range(len(sheep_size)):        #plus 50 after each month
        sheep_size[i] += 50
    print(sheep_size)

print("My current flock has size in total", sum(sheep_size)) #last one
money = sum(sheep_size) * 2
print("i would get", sum(sheep_size), "* 2$ =", money, "$")
