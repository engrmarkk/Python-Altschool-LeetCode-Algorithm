from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rst=[1]*(len(nums))
        prefix=1
        for i in range(len(nums)):
            rst[i]=prefix  
            prefix *=nums[i]
    
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            rst[i]*=postfix #multiplying the result with the postfix
            postfix*=nums[i]
        return rst

solutions=Solution()
lst=[1,2,3,4]
print(solutions.productExceptSelf(lst))