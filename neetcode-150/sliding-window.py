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
    
# Longest Consecutive Substring without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        charSet = set()
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res



        
            