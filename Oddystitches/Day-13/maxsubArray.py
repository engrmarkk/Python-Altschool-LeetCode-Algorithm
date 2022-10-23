from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub= nums[0]
        currentSum= 0
        for i in nums:
            if currentSum<0:
                currentSum=0
            currentSum +=i
            maxSub= max(maxSub, currentSum)
        return maxSub

solutions=Solution()
num=[1,-2,5,9,-6,-4,7]
print(solutions.maxSubArray(num))