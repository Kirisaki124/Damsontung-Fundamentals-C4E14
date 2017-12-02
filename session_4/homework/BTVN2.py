nums = [1, 2, 3, 4, 5, 3, 45, 1, 3, 4]
n = 0
nu = int(input("Enter a number: "))
for i in range(len(nums)):
    if nu == nums[i]:
        n += 1
print(nu, "appear", n, "times")
