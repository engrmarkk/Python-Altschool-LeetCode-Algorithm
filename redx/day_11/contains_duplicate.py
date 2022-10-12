class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for num in nums:
            if len(nums)==len(list(set(nums))):
                return False
                
            return True

fn = Solution().containsDuplicate([1,2,3,1])
fn2 = Solution().containsDuplicate([1,2,3,4])
fn3 = Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2])

print(fn, fn2, fn3)

