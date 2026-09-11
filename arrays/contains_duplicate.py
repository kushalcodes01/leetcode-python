def containsDuplicate(nums):
    seen = []

    for num in nums:
        if num in seen:
            return True

        seen.append(num)

    return False