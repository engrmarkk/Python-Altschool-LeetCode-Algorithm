class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        maxProfit = 0
        min_purchase = prices[0]
        for i in range(1, len(prices)):		
            maxProfit = max(maxProfit, prices[i] - min_purchase)
            min_purchase = min(min_purchase, prices[i])
        return maxProfit

fn = Solution().maxProfit([7,1,5,3,6,4])
fn2 = Solution().maxProfit([7,6,4,3,1])
print(fn, fn2)