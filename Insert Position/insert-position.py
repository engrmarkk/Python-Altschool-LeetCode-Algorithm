"""
 This function searches for a target value in a sorted list of integers and returns the index where it should be inserted.
 It iterates through the list, checking if the target is in the list.
 If it is, the index of the target is returned.
 If not, the function checks if the target is greater than the current element and less than the next element, and if so, returns the index of the next element.
 If the target is greater than the last element, the length of the list is returned, and if it is less than the first element, 0 is returned.
"""
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # sort the list
        nums.sort()
        # check if target is in the list
        if target in nums:
            # return the index of the target
            return nums.index(target)

        # if target is not in the list
        if target not in nums:
            # iterate through the list
            for i in range(len(nums) - 1):
                # check if the target is greater than the current element and less than the next element
                if nums[i] < target and nums[i + 1] > target:
                    # return the index of the next element
                    return i + 1
            # if the target is greater than the last element, return the length of the list
            if nums[len(nums) -1 ] < target:
                # return the length of the list
                return len(nums)
            # if the target is less than the first element, return 0
            if nums[0] > target:
                # return 0
                return 0


solution = Solution()
output = solution.searchInsert([1,3,4,5,7], 8)
print(output)
