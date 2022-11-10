class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        xor = 0
        for num in nums + list(range(1, n+1)):
            xor ^= num
        
        # wich one occered twice
        pos = xor & -xor
        x = 0; y = 0
        for num in nums + list(range(1, n+1)):
            if num & pos:
                x ^= num
            else:
                y ^= num
        
        if nums.count(x) == 2:
            return [x,y]
        return [y,x]
