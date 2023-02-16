class Solution:
    def removeDuplicates(self, nums:list[int]) -> int:
        numbers = 1
        for i in range (1,len (nums)):
            if nums[i-1] != nums[i]:
                nums[numbers] = nums[i]
                numbers+=1
              
            i = i+1
        return numbers
                
solution = Solution()
nums = [1,1,2]
output = solution.removeDuplicates(nums)
print(output)