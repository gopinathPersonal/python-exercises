def runningSum(nums):
    count = 0
    newlist = []
    for item in nums:
        count = count + int(item)
        newlist.append(count)
    return newlist
nums = [2, 3, 5, 1, 3]
n = 3
result = runningSum(nums, 3)
print(result)