nums = [-1, 5, 7, 1, -5]
# j = 0
# x1 = nums[j]
#
# for i, x2 in enumerate(nums):
#     x2 = nums[i]
#     if x1 + x2 == 0:
#         print(nums[j], "+" ,x2, "= 0")
#     j += 1

for i in range(0, len(nums) - 1):
    x1 = nums[i]
    x2 = 0
    found = False
    for j in range(i + 1, len(nums)):
        if x1 + nums[j] == 0:
            x2 = nums[j]
            # print("found", x1, "and", nums[i])
            found = True
            break
    if found:
        print("found {0} and {1}".format(x1, x2))
