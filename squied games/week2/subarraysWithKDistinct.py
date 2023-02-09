class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        #think --> k == 1

        first = defaultdict(int)
        second = defaultdict(int)

        l, r = 0, 0
        res = 0
        for i in range(len(nums)):

            while l < len(nums) and len(first) < k:
                first[nums[l]] += 1
                l += 1
            
            while r < len(nums) and (len(second) + (nums[r] not in first)) <= k:
                second[nums[r]] += 1
                r += 1

            if len(first) == len(second) == k:
                res += r - l + 1

            first[nums[i]] -= 1
            second[nums[i]] -= 1

            if first[nums[i]] == 0:
                del first[nums[i]] 
            
            if second[nums[i]] == 0:
                
                del second[nums[i]]
        
        return res
