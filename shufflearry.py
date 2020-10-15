def shuffle(nums, n):
    newlist =[]
    for item in range(0, n):
        newlist.append(nums[item])
        newlist.append(nums[item + n])
    return newlist
nums = [1,2,3,4,4,3,2,1]
result = shuffle(nums, 4)
print(result)

