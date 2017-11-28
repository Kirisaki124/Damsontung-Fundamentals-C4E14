from random import randint

res = randint(1,101)
count = 0
ans = int(input("number?"))
while count < 7:
    while ans != res:
        if ans > res:
            print("too large")
        else:
            print("too small")
            count += 1
            ans = int(input("number?"))
    print("you lost the game")

print("bingo")
