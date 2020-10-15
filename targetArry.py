class Solution:
    def createTargetArray(self, nums, index):
        newtarget = []
        for i in nums:
            newtarget.insert(index[i],i)
        return newtarget


a = Solution()
result = a.createTargetArray([1,2,3,4,0], [0,1,2,3,0])
print(result)