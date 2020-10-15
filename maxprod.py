class Solution:
    def maxProduct(self, nums):
        lent = len(nums)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
        maxp = (nums[lent-2] - 1) * (nums[lent-1] -1)
        return(maxp)

a = Solution()
result = a.maxProduct([3,7])
print(result)