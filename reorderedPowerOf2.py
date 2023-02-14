class Solution:
    def same_count(self, a, b):
        if len(a) != len(b):
            return False
            
        for key in a:
            if key not in b or b[key] != a[key]:
                return False
        return True 
    def reorderedPowerOf2(self, n: int) -> bool:
        freq = Counter(str(n))
        for i in range(31):
            if self.same_count(freq, Counter(str(1<<i))):
                print(1<<i)
                return True        
        return False
                    
