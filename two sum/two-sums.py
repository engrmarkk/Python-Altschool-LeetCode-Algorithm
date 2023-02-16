"""
 This function takes a list of integers and a target integer as parameters and returns a list of two indices that sum up to the target.
 It iterates through the list of numbers and checks if the sum of any two numbers in the list equals the target.
 If it does, it returns the indices of the two numbers.
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # y is the length of the list of numbers
        y = len(nums)
        # h is the index of the first number in the list
        # f is the list of numbers after the first number
        # x is the index of the second number in the list
        # iterate through the list of numbers
        for i in range(y):
            h = i+1
            f = nums[h:]
            # iterate through the list of numbers after the first number
            for x in range(len(f)):
                # if the sum of the two numbers equals the target, return the indices of the two numbers
                if nums[i] + f[x] == target:
                    # add 1 to the index of the second number because the list of numbers after the first number starts at index 0
                    return [i, x+h]
            else:
                # if the sum of the two numbers does not equal the target,
                # continue to the next iteration of the loop
                continue



                
solution = Solution()
nums = [3,2,2,3]
target = 6
print(solution.twoSum(nums, target))
