"""
 This function removes the given value (val) from the given list of numbers (nums) and prints the resulting list.
 It iterates through the list and if the value is found, it is removed from the list.
"""
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # iterate through the list
        for num in list(nums):
            # if the value is found, remove it from the list
            if num == val:
                # remove the value from the list
                nums.remove(num)
            # if the value is not found, continue to the next value
            else:
                # continue to the next value
                continue
        
        print(nums)


solution = Solution()
output = solution.removeElement([0,1,2,2,3,0,4,2,2,2,2], 2)
print(output)
