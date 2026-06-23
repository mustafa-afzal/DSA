# Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        map = {")": "(", "]": "[", "}": "{"}
        stack = []
        for char in range(len(s)):
            if s[char] in map and stack and stack[-1] == map[s[char]]:
                stack.pop()
            else:
                stack.append(s[char])
        return not stack

# Min Stack



