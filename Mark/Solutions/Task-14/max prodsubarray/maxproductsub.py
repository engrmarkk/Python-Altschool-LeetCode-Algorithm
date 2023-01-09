class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        result = max(nums)
        currentMinimun, currentMaximum = 1, 1

        for num in nums:
            temp = currentMaximum * num
            currentMaximum = max(num * currentMaximum, num * currentMinimun, num)
            currentMinimun = min(temp, num * currentMinimun, num)
            result = max(result, currentMaximum)
        return result

output = Solution().maxProduct([-3,-1,-1])
# output = Solution().maxProduct([-1,0,-1])
# output = Solution().maxProduct([0,2])
print(output)
