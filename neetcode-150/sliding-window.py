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
    
# Longest Repeating Character Replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        dict1 = {}
        for r in range(len(s)):
            if s[r] in dict1:
                dict1[s[r]] += 1
            else:
                dict1[s[r]] = 1
            windowSize = r - l + 1
            maxFreq = max(dict1.values())
            if windowSize - maxFreq > k:
                dict1[s[l]] -= 1
                l += 1
            else:
                res = max(res, windowSize)
        return res

# Permutation in String

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        map1 = {}
        map2 = {}
        k = len(s1)
        for i in range(len(s1)):
            if s1[i] in map1:
                map1[s1[i]] += 1
            else:
                map1[s1[i]] = 1
        for i in range(k):
            if s2[i] in map2:
                map2[s2[i]] += 1
            else:
                map2[s2[i]] = 1
        for i in range(0, len(s2) - k):
            if map1 == map2: return True
            if s2[i+k] in map2:
                map2[s2[i+k]] += 1
            else:
                map2[s2[i+k]] = 1
            map2[s2[i]] -= 1
            if map2[s2[i]] == 0:
                del map2[s2[i]]
        return map1 == map2

# Minimum Window Substring

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        resL = 0
        resR = 0
        seenS = {}
        seenT = {}
        need = len(set(t))
        have = 0
        minWindowLen = float('inf')
        seenT = Counter(t)
        for r in range(len(s)):
            seenS[s[r]] = seenS.get(s[r], 0) + 1
            if seenT[s[r]] and seenS[s[r]] == seenT[s[r]]:
                have += 1
            while have == need:
                windowLen = r - l + 1
                if windowLen < minWindowLen:
                    minWindowLen = windowLen
                    resL = l
                    resR = r
                seenS[s[l]] = seenS.get(s[l], 0) - 1
                if seenS[s[l]] < seenT[s[l]]:
                    have -= 1
                l += 1
        if minWindowLen == float('inf'):
            return ""
        return s[resL : resR + 1]
                
            
        
        
            
            





        
            