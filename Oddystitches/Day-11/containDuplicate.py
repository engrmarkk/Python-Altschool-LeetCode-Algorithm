from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_num=set(nums)
        if len(nums)==len(new_num):
            return False
        else:
            return True


solutions=Solution()
num=[1,2,3,1]
print(solutions.containsDuplicate(num))