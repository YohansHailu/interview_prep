class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(n):
                if i != j:
                    count += nums[i] + nums[j] == target
        
        return count
