class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        for op in logs:
            if op == "./":
                continue
            if op == "../":
                if res:
                    res -= 1
                continue
            res += 1 
        return res   
