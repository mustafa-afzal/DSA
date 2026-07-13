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