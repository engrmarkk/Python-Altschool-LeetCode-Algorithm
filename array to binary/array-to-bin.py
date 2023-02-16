# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
 This function takes in a sorted array of numbers and returns a binary search tree.
 It uses a recursive approach to create the tree by finding the middle point of the array and creating a node with that value.
 The left and right subtrees are then created by recursively calling the function with the left and right halves of the array.
"""
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Base case
        def convert(left, right):
            # If the left and right pointers are equal, then the array is empty and we return None
            if right == left:
                return TreeNode(nums[left])
            # if the left pointer is greater than the right pointer, then the array is empty and we return None
            if right < left:
                return None

            # Find the middle point of the array
            middle = (right + left) // 2
            # Create a node with the value of the middle point
            return TreeNode(val = nums[middle], left = convert(left, middle - 1), right = convert(middle + 1, right))
        # return the root of the tree
        return convert(0, len(nums) - 1)
    
    
Solution().sortedArrayToBST([1, 3])
