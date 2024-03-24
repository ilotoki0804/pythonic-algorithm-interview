class Solution:
    def isPalindrome(self, string: str) -> bool:
        chars = [char.lower() for char in string if char.isalnum()]

        # 팰린드롬 여부 판별
        while len(chars) > 1:
            if chars.pop(0) != chars.pop():
                return False

        return True
