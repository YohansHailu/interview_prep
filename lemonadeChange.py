class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = {5:0,10:0,20:0} 
        # yes
        for val in bills:
            target = val - 5
            for change in  [20,10,5]:
                
                if target >= change:
                    count = min(changes[change], target//change)
                    changes[change] -= count
                    target -= change * count
                    
            if target > 0:
                return False
            
            changes[val] += 1 
            print(val, changes)        
        return True
