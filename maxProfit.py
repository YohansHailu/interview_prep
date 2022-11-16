class Solution:
    def get_best_limit(self, arr, target):
    
        total_sum = sum(arr)
        left = 0; right = arr[-1]
        best = right 
        while left <= right:
            mid = (left + right)//2
            
            limit_sum = 0
            for val in arr:
                limit_sum += min(val, mid)
                
            diff = total_sum - limit_sum
            
            if diff == target:
                return mid
            
            if diff > target:
                left = mid + 1
                
            elif diff < target:     
                best = mid
                right = mid - 1
                
        return best 
           
        
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        Mod = 10**9 + 7
        inventory.sort()
        k = self.get_best_limit(inventory, orders)
        res = 0
        for val in inventory:
            if val > k:
                sold = val - k
                orders -= sold
                cost = ((val + k + 1) * (val - k))//2
                res = (res + cost)%Mod
                
        res += orders * k
        return res%Mod
        
        
