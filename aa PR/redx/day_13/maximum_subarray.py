class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum

fn = Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
fn2 = Solution().maxSubArray([1])
fn3 = Solution().maxSubArray([5,4,-1,7,8])
print(fn, fn2, fn3)