# (()(()))

# 3
# res  = 1 --> you should add 2 --> 6

# add mark and double makr

# (())
# if zero add one
# 
# add --> 
# stack = [4]
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        
        val = 0
        
        for c in s:
            if c == "(":
                stack.append( 0 )
            
            if c == ")":
                val = stack.pop()
                if stack:
                    stack[-1] += 2*val if val else 1             
           
        return stack[0]