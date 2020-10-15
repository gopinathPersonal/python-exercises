num = 234
nums = []
while num >= 1:
    nums.append(num % 10)
    num = num // 10
print(nums)