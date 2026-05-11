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