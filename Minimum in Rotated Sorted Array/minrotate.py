
class Solution:
    def findMin(self, nums: list[int]) -> int:
        # takes the first number in the array
        res = nums[0]
        # set the value to be 0 and lenght minus 1 respectively
        l, r = 0, len(nums) -1

        # while l is less than or equals r
        while l <= r:
            # check if the number at the index of the value of l is less than the number at the index of rhe value of r
            if nums[l] < nums[r]:
                # if yes, res takes the minimum value between the initial value of res and the number at the index of the value of l
                res = min(res, nums[l])
                # and break out of the loop
                break

            # m take the middle number
            m = (l + r) // 2
            # res take the miinimum of the initial value of res and number at the index of m
            res = min(res, nums[m])
            # number at the index of the value of m is greater than or equals to to the number at the index of the value of l
            if nums[m] >= nums[l]:
                # l take the value of m + 1
                l = m + 1
            else:
                # else, r takes the value of m -1
                r = m - 1
        # return the res
        return res


output = Solution().findMin([3,5,1])
print(output)

'''
[3,4,5,1,2]

[4,5,1,2,3]

[4,5,6,7,0,1,2]

[11,13,15,17]
'''

