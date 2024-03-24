from collections import deque


class Solution:
    def isPalindrome(self, string: str) -> bool:
        chars = deque(char.lower() for char in string if char.isalnum())

        while len(chars) > 1:
            if chars.popleft() != chars.pop():
                return False

        return True
