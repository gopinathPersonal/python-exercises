class Solution:
    def decompressRLElist(self, nums):
        n = len(nums)
        newarr=[]
        for i in range(0,n,2):
            m = nums[i]
            for j in range(m):
                newarr.append(nums[i+1])
        return newarr


a = Solution()
result = a.decompressRLElist([1, 2, 6, 3, 4, 10, 1, 5, 5, 3])
print(result)