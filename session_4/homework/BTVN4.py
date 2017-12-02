B = int(input("How many bacterias?"))
time = int(input("How much times (minutes)?"))

result = (time/2)*B

if time % 2 != 0:
    print("not sure")
    print("maybe", result)
else:
    print("After {0} minutes, we would have {1} bacterias".format(time, result))
