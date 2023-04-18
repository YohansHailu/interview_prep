class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for j  in range(min(len(word1), len(word2))):
            res += word1[j]
            res += word2[j]
        
        return res + (word2[j+1:] or word1[j+1:]) 
        