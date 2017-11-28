
menu = ["deathnote", "netflix", "teaching"]

for i, item in enumerate(menu):
    print(i + 1, menu[i], sep=". ")

rem = input("what do u want to delete")
if rem in menu:
    menu.remove(rem)
    for i, item in enumerate(menu):
        print(i + 1, menu[i], sep=". ")
else:
    print("failed")
#buggggg
