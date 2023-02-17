class Solution:
    def firstUniqChar(self, s: str) -> int:

        freq = Counter(s)
        for i in range(len(s)):
            if freq[s[i]] < 2:
                return i
        
        return -1
