class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1
        for i in range(len(digits))[::-1]:
            val = (digits[i] + carry)%10
            carry = (digits[i] + carry)//10
            digits[i] = val
            
        if carry:
            return [carry] + digits
        
        return digits
