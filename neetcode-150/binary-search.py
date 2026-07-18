# Binary Search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, (len(nums) - 1)
        while l <= r:
            mid = (r + l) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        return -1

# Search a 2D Matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l, r = 0, (rows * cols - 1)
        while l <= r:
            mid = (l + r) // 2
            rowMid = mid // cols
            colMid = mid % cols
            if target < matrix[rowMid][colMid]:
                r = mid - 1
            elif target > matrix[rowMid][colMid]:
                l = mid + 1
            else:
                return True
        return False
    
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        if not (top <= bot):
            return False
        l, r = 0, COLS - 1
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        return False

# Koko Eating Bananas

import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minK = max(piles)
        while l <= r:
            mid = (l + r) // 2
            pileTime = 0
            for i in range(len(piles)):
                pileTime += math.ceil(piles[i] / mid)
            if pileTime <= h:
                minK = min(mid, minK)
                r = mid - 1
            else:
                l = mid + 1
        return minK

# Find Minimum in Rotated Sorted Array

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(nums[l], res)
                break
            
            m = (l + r) // 2
            res = min(nums[m], res)
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res

# Search in Rotated Sorted Array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > nums[r]:
                if target <= nums[m] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] <= nums[r]:
                if target >= nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1

# Time Based Key-Value Store

class TimeMap:

    def __init__(self):
        self.hmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.hmap.get(key):
            self.hmap[key].append((timestamp, value))
        else:
            self.hmap[key] = []
            self.hmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.hmap.get(key)
        bestVal = -1
        if pairs:
            length = len(pairs)
        else:
            length = 0
        l, r = 0, length - 1
        while l <= r:
            m = (l + r) // 2
            if pairs[m][0] > timestamp:
                r = m - 1
            elif pairs[m][0] <= timestamp:
                bestVal = pairs[m][1]
                l = m + 1
        return bestVal if bestVal != -1 else ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# Median of Two Sorted Arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i + 1] if i + 1 < len(A) else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j + 1] if j + 1 < len(B) else float('inf')
            
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1