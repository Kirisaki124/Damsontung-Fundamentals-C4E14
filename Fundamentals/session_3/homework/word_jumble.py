from random import shuffle
import random

word = ["tung", "trang", "linh", "uyen", "hieu", "tien"]

print()                                    #shuffle character
name = random.choice(word)
character = list(name)
shuffle(character)
print(character)

while True:
    ans = input("guess a name?")
    if ans == name:
        print("bingo")
        break
    else:
        print("guess again")
