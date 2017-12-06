menu = ["a", "b", "c"]
# for i in range(len(menu)):
# enumerate
for i, item in enumerate(menu):

    print(i + 1, item, sep=". ")

num = int(input("which number do u want to change?"))

cge = input("what do u want to change to?")

menu[num - 1] = cge

for i, menu in enumerate(menu):
    print(i + 1, menu, sep=". ")
