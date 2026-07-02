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
