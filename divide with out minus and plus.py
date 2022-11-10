class Solution:
    def add(self, x,y):
        carry = 0
        res = 0
        for i in range(34):
            a = x & 1<<i
            b = y & 1<<i
            cur = a ^ b ^ carry
            res |= cur
            carry = (a & b) | ((a | b) & carry)
            carry <<= 1
        return res
    
    def change_sign(self, num):
        return ~num + 1
    
    def divide(self, a: int, b: int) -> int:
        sign = -1 if (a < 0 and b > 0 or a > 0 and b < 0) else 0
        if a < 0: 
            a = self.change_sign(a)
            
        if b < 0: 
            b = self.change_sign(b)
            
        cur = b 
        count = 1
        while cur <= a:
            # something that doubles ad resets
            cur = self.add(cur, b)
            count += 1
            db = 2*b 
            while self.add(cur, db) <= a:
                cur = self.add(cur, db)
                count += db//b
                db <<= 1
            
            
        ans  = count - 1
        if sign < 0:
            ans = self.change_sign(ans) 
         
        return max(min(ans, 2**31 - 1), -2**31)
