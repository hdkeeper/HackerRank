def group_numbers(nums):
    if not nums:
        return ""
    nums = sorted(nums)
    result = []
    start = prev = nums[0]
    for num in nums[1:]:
        if num == prev + 1:
            prev = num
        else:
            if start == prev:
                result.append(str(start))
            else:
                result.append(f"{start}-{prev}")
            start = prev = num
    if start == prev:
        result.append(str(start))
    else:
        result.append(f"{start}-{prev}")
    return ",".join(result)

print(group_numbers([1, 2, 3, 5, 6, 8, 9, 10, 12]))
