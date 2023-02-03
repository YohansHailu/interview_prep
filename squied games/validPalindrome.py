class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True

        left = 0
        right = len(s) - 1
        jumps = 0
        while left <= right:

            if s[left] != s[right]:
                no_left = s[:left] + s[left + 1:]
                no_right = s[:right] + s[right + 1:]
                return no_left == no_left[::-1] or no_right == no_right[::-1]
                
            left += 1 
            right -= 1

        return True
