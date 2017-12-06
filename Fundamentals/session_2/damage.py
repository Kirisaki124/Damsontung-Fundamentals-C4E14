from random import *


luck = int(input("luck? "))
agi = int(input("agi? "))
cube = randint(1,6)


if luck + agi > cube:
    print("not hit")
else:
    print("hit")
