class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        sums = []
        cur = 0
        for val in nums:
            cur += val
            if cur < val:
                cur = val
            sums.append(cur)
         
        return max(sums) 
