def runningSum(nums, n):
    val1 = 'true'
    max = nums[0]
    printlist = []
    for i in range(1,len(nums)):
        if(nums[i] > max):
            max = nums[i]
    for j in range(0, len(nums)):
        if(nums[j]+ n >= max):
            printlist.append(val1)
        else:
            printlist.append(str(False).lower())
    return printlist

nums = [2, 3, 5, 1, 3]
n = 3
result = runningSum(nums, 3)
print(result)