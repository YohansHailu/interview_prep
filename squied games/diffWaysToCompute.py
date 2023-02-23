class Solution:
    def diffWaysToCompute(self, exp: str) -> List[int]:
        
        is_num = True
        res = []
        for i in range(len(exp)):
            
            if exp[i] not in ["*","-","+"]:
                continue
                
            is_num = False     
            
            op = exp[i]
            for a in self.diffWaysToCompute(exp[:i]):
                for b in self.diffWaysToCompute(exp[i+1:]):
                    res.append(eval(str(a) + op + str(b)))
        if is_num:            
            return [int(exp)]
        return res
