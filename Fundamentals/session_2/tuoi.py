n = int(input("nam sinh "))
t = 2017 - n
print("ban", t, "tuoi")

if t < 10:
    print("baby")
elif t < 18:
    print("teenage")
else:
    print("adult")
