# Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        cheapest = prices[0]
        for i in range(len(prices)):
            cheapest = min(prices[i], cheapest)
            profit = prices[i] - cheapest
            maxP = max(profit, maxP)
        return maxP