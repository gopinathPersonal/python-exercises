class Solution:
    def smallerNumbersThanCurrent(self, nums):
        newls =[]
        count = 0
        for i in range(0,len(nums)):
            for j in range(0, len(nums)):
                if nums[i] > nums[j]:
                    count += 1
            newls.append(count)
            count = 0
        return newls

a = Solution()
result = a.smallerNumbersThanCurrent([6, 5, 4, 8])
print(result)