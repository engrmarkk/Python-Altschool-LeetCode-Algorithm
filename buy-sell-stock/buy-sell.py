"""
 This function finds the maximum profit that can be made from a given list of prices.
 It iterates through the list, comparing the current index to the next index, and calculating the difference between them.
 If the difference is positive, it updates the maximum profit with the difference.
 If the difference is negative, the current index is updated to the next index.
 The function returns the maximum profit.
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # assign the first index to the current index, the second index to the next index, and the maximum profit to 0
        currentIndex, nextIndex, maxProfit = 0, 1, 0

        # iterate through the list
        while nextIndex < len(prices):
            # if the price at the next index is greater than the price at the current index, calculate the profit
            if prices[currentIndex] < prices[nextIndex]:
                # profit = price at next index - price at current index
                profit = prices[nextIndex] - prices[currentIndex]
                # update the maximum profit with the profit
                maxProfit = max(maxProfit, profit)
            # if the price at the next index is less than the price at the current index, update the current index to the next index
            else:
                # current index = next index
                currentIndex = nextIndex
            # increment the next index
            nextIndex += 1
        # return the maximum profit
        return maxProfit

solution = Solution().maxProfit([7,1,5,3,6,4])
print(solution)
