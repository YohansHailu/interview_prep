class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        #l = -1 
        #r = -1
        a.reverse()
        b.reverse()
        
        n = len(a) + len(b)
        
        pre_mid = 0
        mid = 0  
        
        i = 0
        while i <= n//2 and a and b:
            pre_mid = mid
            mid = a.pop() if a[-1] < b[-1] else b.pop()
            i += 1
        while i <= n//2 and a:
            pre_mid = mid
            mid = a.pop(); i += 1
        while i <= n//2 and b: 
            pre_mid = mid
            mid = b.pop(); i += 1
        
        if n % 2 == 1:
            return mid
        return (pre_mid + mid) /2
