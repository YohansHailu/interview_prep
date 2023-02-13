class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aval = 0
        for i in range(len(a)):
            aval += int(a[i])*2**(len(a)-i-1)
        
        bval = 0
        for i in range(len(b)):
            bval += int(b[i])*2**(len(b)-i-1)
            
        return bin(aval+bval)[2:]
