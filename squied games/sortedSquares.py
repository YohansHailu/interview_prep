class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqr = []
        for i in nums:
            sqr.append(i*i)
                    
               
        sqr.sort()            
        return sqr
