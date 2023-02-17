class Solution:
    def valied(self, s):
        bal = 0
        for i in s:
            bal += 1 if i == "(" else -1
            if bal < 0: return False
        return bal == 0
    
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        l = (1<<2*n)
        
        for i in range(l):
            sub = []
            for j in range(2*n):
                sub.append("(" if( 1 << j & i) else ")")
            if self.valied(sub):
                ans.append("".join(sub))
        
        return ans
