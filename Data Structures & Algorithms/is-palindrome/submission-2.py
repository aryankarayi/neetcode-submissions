class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ''
        for char in s:
            if char.isalnum() and char != ' ':
                new += char.lower()
        return new == new[::-1]
        