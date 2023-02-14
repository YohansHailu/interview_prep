class Solution:
    def dp_helper(self, i, num_a, s):
        if i >= len(s):
            return 0
        
        
        if s[i] == "a":
            return self.dp_helper(i+1, num_a - 1, s)
        
        if num_a == 0: 
            return 0
        
        # its b now 
        no_delete = num_a
        delete = self.dp_helper(i+1, num_a, s) + 1
        return min(no_delete, delete)
            
        
    def minimumDeletions(self, s: str) -> int:
        return self.dp_helper(0, list(s).count("a"), s)
        
