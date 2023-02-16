"""
Given an integer array nums that may contain duplicates, return all possible subsets 
(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""

from itertools import combinations


"""
This code generates all possible subsets of a given list of numbers, including duplicates. 
It uses the combinations() function from the itertools module to generate all possible subsets. 
The resulting list is then sorted and any duplicates are removed. 
Finally, the list of unique subsets is returned.
"""

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        # define empty lists
        new_list = []
        # define empty list to store unique subsets
        final_list = []
        # iterate through the length of the list
        for i in range(len(nums) + 1):
            # generate all possible subsets of the list
            new_list += [list(j) for j in combinations(list(nums), i)]

        # iterate through the list of subsets
        for each_list in list(new_list):
            # sort each subset
            each_list = sorted(each_list)
            # check if the subset is unique
            if each_list not in final_list:
                # if unique, add to the final list
                final_list.append(each_list)

        # return the list of unique subsets
        return final_list


solution = Solution()
output = solution.subsetsWithDup([4,4,4,1,4])
print(output)
