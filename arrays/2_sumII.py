def twoSum(nums, target):

    seen ={}

    for i in range(len(nums)):

        current = nums[i]
        needed = target - current

        if needed in seen:
            return [seen[needed], i]

        seen[current] = i 

print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))