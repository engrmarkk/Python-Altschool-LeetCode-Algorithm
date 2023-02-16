"""
This function takes two lists of integers, nums1 and nums2, and two integers, m and n, as parameters.
It modifies nums1 in-place by merging the two lists and sorting them in ascending order.
No return value is given.
"""
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2)


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
output = Solution().merge(nums1, m, nums2, n)
