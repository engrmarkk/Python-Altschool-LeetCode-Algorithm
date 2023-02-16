"""
 This code is used to remove duplicate elements from a list of numbers.
 It iterates through the list and compares each element to the next one.
 If the current element is less than the next one, it is added to a new list.
 The new list is then returned, containing only the distinct elements.
"""
"""
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
"""
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # dif_num is the number of distinct elements in the list
        dif_num=1
        # if the list is empty, return 0
        if nums==[]:
            return 0

        # iterate through the list of numbers
        for i in range(len(nums)):
            # if the current element is less than the next one, add it to the new list
            if(i+1<len(nums)):
                # if the current element is less than the next one, add it to the new list
                if nums[i]<nums[i+1]:
                    # add the current element to the new list
                    nums[dif_num]=nums[i+1]
                    # add 1 to the number of distinct elements in the list
                    dif_num+=1
            
        print(nums)
        # return the number of distinct elements in the list
        return dif_num


solution = Solution()
output = solution.removeDuplicates([1,1,1,1,1,1])
print(output)
