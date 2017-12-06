nums = [-20, 20, 34, 432, 12]
x = int(input("number"))

found = False
found_index = -1

for index, num in enumerate(nums):
    if num == x:
        # print("found {0} at {1}".format(x, index))
        found_index = index
        found = True
        break
if not found:
    print("not found")
else:
    print("found {0} at {1}".format(x, index))
