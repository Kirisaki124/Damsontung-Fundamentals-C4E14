nums = [-2, 0 ,-342 ,2 ,3]

# print(min(nums))

minn = nums[0]
for num in nums:
    if minn > num:
        minn = num

print(minn)
