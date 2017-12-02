x = "ThiS is String with Upper and lower case Letters"

# alp = "abcdefghijklmnopqrstuvwxwz"
# list(alp)

letters = {}
for letter in x:
    letters[letter] = letters.get(letter, 0) + 1
print(letters)

# print("a ", list(x).count("a") + list(x).count("A"))
# print("c ", list(x).count("c") + list(x).count("C"))
# print("d ", list(x).count("d") + list(x).count("D"))
# print("e ", list(x).count("e") + list(x).count("E"))
# print("g ", list(x).count("g") + list(x).count("G"))
# print("h ", list(x).count("h") + list(x).count("H"))
# print("i ", list(x).count("i") + list(x).count("I"))
# print("l ", list(x).count("l") + list(x).count("L"))
# print("n ", list(x).count("n") + list(x).count("N"))
# print("o ", list(x).count("o") + list(x).count("O"))
# print("p ", list(x).count("p") + list(x).count("P"))
# print("r ", list(x).count("r") + list(x).count("R"))
# print("s ", list(x).count("s") + list(x).count("S"))
# print("t ", list(x).count("t") + list(x).count("Y"))
# print("u ", list(x).count("u") + list(x).count("U"))
# print("w ", list(x).count("w") + list(x).count("W"))
