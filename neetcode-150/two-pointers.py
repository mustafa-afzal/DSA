# Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        sLower = s.lower()
        while l < r:
            if sLower[l].isalnum() and sLower[r].isalnum() and sLower[l] == sLower[r]:
                l += 1
                r -= 1
            elif not sLower[l].isalnum():
                l += 1
            elif not sLower[r].isalnum():
                r -= 1
            else:
                return False
        return True
    
# Two Sum II Input Array is Sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[r] + numbers[l] == target:
                return [l+1, r+1]
            elif numbers[r] + numbers[l] < target:
                l += 1
            else:
                r -= 1

# 3Sum 

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        res = []
        r = len(nums) - 1
        for i in range(0, r):
            l, r = i + 1, len(nums) - 1
            if i != 0 and nums[i] == nums[i-1]:
                continue
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else :
                    l += 1
        return res

# Container with Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxA = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            maxA = max(area, maxA)
        return maxA


# Trapping Rain Water

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        trapped = 0
        while l <= r:
            if leftMax <= rightMax:
                leftMax = max(leftMax, height[l])
                trapped += leftMax - height[l]
                l += 1
            else:
                rightMax = max(rightMax, height[r])
                trapped += rightMax - height[r]
                r -= 1
        return trapped



        