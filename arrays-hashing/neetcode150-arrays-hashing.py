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

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for s in strs:
            sSorted = "".join(sorted(s))
            if sSorted in map:
                map[sSorted].append(s)
            else:
                map[sSorted] = [s]
        return (list(map.values())) 

# Top K Freq Elements

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqNums = Counter(nums)
        numsSorted = sorted(freqNums.items(), 
            key = lambda x: x[1], reverse=True)
        topKeys = []
        for i in numsSorted[:k]:
            key = i[0]
            topKeys.append(key)
        return topKeys


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

# Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prod = 1
        for i in range(len(nums)):
            res[i] = prod
            prod *= nums[i]
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= prod
            prod *= nums[i]
        return res
    
# Valid Sudoku

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[r // 3, c // 3]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[r // 3, c // 3].add(board[r][c])
        return True
        