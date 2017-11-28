menu = ["a","b","c"]

for i, item in enumerate(menu):
    print(i + 1, item, sep=". ")

delete = int(input("number to delete"))
del menu[delete - 1]

for i, item in enumerate(menu):
    print(i + 1, item, sep=". ")
