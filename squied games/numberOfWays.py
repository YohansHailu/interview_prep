class Solution:
    def numberOfWays(self, s: str) -> int:
        # count 101 and 010

        # prefix sum


        # count 010 s

        #0 --> 01 --> 010 


        # iteraite

        # if you find 1 --> add that much to 01
        # if you find 0 add that much to 010

        zero = 0
        zeroOne = 0
        zeroOneZero = 0

        
        for i in range(len(s)):
            
            if s[i] == "0":
                zeroOneZero += zeroOne
                zero += 1
            if s[i] == "1":
                zeroOne += zero
        
        one = 0
        oneZero = 0
        oneZeroOne = 0

        
        for i in range(len(s)):
            
            if s[i] == "1":
                oneZeroOne += oneZero
                one += 1
            if s[i] == "0":
                oneZero += one
        
        return oneZeroOne + zeroOneZero
