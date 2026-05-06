# Contains Duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsSet = set(nums)
        return not len(numsSet) == len(nums)
    
# Valid Anagram

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS = Counter(s)
        freqT = Counter(t)
        return freqS == freqT
    
# Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, v in enumerate(nums):
            comp = target - v
            if comp in map:
                return [i, map[comp]]
            map[v] = i