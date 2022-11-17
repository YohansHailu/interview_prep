class Solution:
    def romanToInt(self, s: str) -> int:
        #if I becams just before V
        #if X is befere L or C
        
        values = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        
        res = 0 
        for i in range(len(s)):
            if s[i:i+2]  in ["IV","IX","XL","XC","CD","CM"]:
                res -= values[s[i]]
                continue
                
            res += values[s[i]]
            
        return res
