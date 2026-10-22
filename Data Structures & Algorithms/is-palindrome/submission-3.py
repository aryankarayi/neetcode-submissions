class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        for char in s:
            if char.isalnum():
                new_s += char.lower()

        l, r = 0, len(new_s) - 1
        while l < len(new_s):
            if new_s[l] != new_s[r]:
                return False
            else:
                r -= 1
                l += 1
        return True

        