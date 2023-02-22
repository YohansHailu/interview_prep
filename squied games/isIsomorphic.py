class Solution:
    def isIsomorphic(self, a: str, b: str) -> bool:
        if len(a) !=  len(b):
            return False
        
        visited = set()
        maping = dict()
        for i, ch in enumerate(a):
            
            if ch in maping:
                if maping[ch] != b[i]: return False
                continue
            if b[i] in visited:
                return False
            
            maping[ch] = b[i]
            visited.add(b[i])
            
        return True 
