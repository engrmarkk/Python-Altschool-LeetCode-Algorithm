class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        maxProfit = 0
        min_purchase = prices[0]
        for i in range(1, len(prices)):		
            maxProfit = max(maxProfit, prices[i] - min_purchase)
            min_purchase = min(min_purchase, prices[i])
        return maxProfit