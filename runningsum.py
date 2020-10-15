def runningSum(nums):
    count = 0
    newlist = []
    for item in nums:
        count = count + int(item)
        newlist.append(count)
    return newlist
nums = [3, 1, 2, 10, 1]
result = runningSum(nums)
print(result)