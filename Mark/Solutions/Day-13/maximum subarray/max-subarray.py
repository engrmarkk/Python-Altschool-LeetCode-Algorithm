class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSubArr = nums[0]
        current = 0

        for num in nums:
            if current < 0:
                current = 0
            current += num
            maxSubArr = max(maxSubArr, current)
        return maxSubArr


Solution = Solution()
output = Solution.maxSubArray([-2, 2, 3, 4 -8, 8])
print(output)
