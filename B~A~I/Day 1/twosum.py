class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list [int]:
        y = len(nums)
        for i in range(y):
            h = i+1
            f = nums[h:]
            for x in range(len(f)):
                if nums[i] + f[x] == target:
                    return [nums[i], nums[x+h]]
                else:
                    continue
                    
                    
solution=Solution()                
incomig = [2,7,11,15]
tar = 9
print(solution.twoSum(incomig,tar))
    