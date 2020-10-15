class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = []
        while n >= 1:
            nums.append(n % 10)
            n = n // 10
        summ = 0
        diff = 0
        prod = 1
        for i in nums:
            summ = summ + i
            prod = prod * i
        diff = prod - summ
        return diff


a = Solution()
result = a.subtractProductAndSum(234)
print(result)