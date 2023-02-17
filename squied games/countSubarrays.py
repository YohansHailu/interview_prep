class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # widen if mn greate and max less
            # if hit the best
            # move left you you drope the min or the max the start widengin
        # if the current is less then min or greater then max    
        
        # if in a way find this bad  number just start over
        valiedCount = [0 for i in nums]
        valiedCount[-1] =  minK <= nums[-1] <= maxK
        for i in range(len(nums)-1)[::-1]:
            if minK <= nums[i] <= maxK:
                valiedCount[i] = 1 + valiedCount[i+1]
        print(valiedCount)        
        minCount = 0
        maxCount = 0 
        res = 0
        
        left = 0
        for i in range(len(nums)):
            val = nums[i]
            if val < minK or val > maxK:
                minCount = 0 
                maxCount = 0 
                left = i+1
                continue
                
            minCount += val ==  minK    
            maxCount += val ==  maxK    
            while minCount > 0 and maxCount > 0:
                if minCount > 0 and maxCount > 0:
                    res += valiedCount[i]
                minCount -= nums[left] ==  minK    
                maxCount -= nums[left] ==  maxK    
                left += 1
                
        return res  
