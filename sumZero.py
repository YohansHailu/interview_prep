class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = []
        # the remove zero
        for i in range(n//2):
            arr.append(i + 1)
            arr.append(-(i+1))
        
        if n%2:
            arr.append(0)
        
        return arr
