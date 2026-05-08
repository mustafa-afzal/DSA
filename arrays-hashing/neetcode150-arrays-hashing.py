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

# Group Anagrams

# Encode and Decode Strings

class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += str(len(i)) + "#" + i
        return s
      
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length - 1
            res.append(s[i:j+1])
            i = j + 1
        return res