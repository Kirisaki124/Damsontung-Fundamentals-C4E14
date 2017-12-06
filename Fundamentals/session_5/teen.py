teencode = {
    "bb": "bạn bè",
    "kcj": "không có gì",
    "vl": "vãi l**",

}
while True:
    for key, value in teencode.items():
        print(key, end=" ")
    print()

    inp = str(input("muốn search gì")).lower()

    if inp in teencode.keys():
        print(inp)
        print(teencode[inp])
    else:
        choice = input("not found wanna add (Y/N)")
        if choice == "Y" or choice == "y"
            translation = input("add to")
            teencode[inp] = translation
