nums = [1, 2, 3, 4, 5, 6, 7]

found = False
lo = 0
hi = len(nums)

guess = int(input("number?"))

while hi > lo:
    mid = (lo + hi) // 2
    num = nums[mid]
    if guess == num:
        found = True
        break
        print("found")
    elif guess < num:
        hi = mid
        print("left")
        print(lo, hi)
    else:
        lo = mid + 1
        print("right")
        print(lo, hi)
    if not found:
        print("not found")
