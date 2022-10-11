from typing import List
class Solution():
    def maxProfit(self, prices: List[int]) -> int:
        leftIndex=0
        rightIndex=1
        maxP=0

        while rightIndex<len(prices):
            if prices[leftIndex]<prices[rightIndex]:
                profit=prices[rightIndex]-prices[leftIndex]
                maxP=max(maxP, profit)
            else:
                leftIndex=rightIndex
        
            rightIndex+=1
        return maxP
num= Solution()
price=[2,4,1]
print(num.maxProfit(price))