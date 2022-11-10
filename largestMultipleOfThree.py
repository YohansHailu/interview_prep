class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        # bottom up
        # and choose path
        
        digits.sort(reverse = True)
        
        n = len(digits)
        dp = [[0]*3 for _ in range(n + 1)]
        dp[n][0] = 1
        # fill all the sums
        # take or don't tkae for the last index
        for i in range(n)[::-1]:
            for sm in range(3):
                take_sum = (sm + digits[i])%3
                take_it = dp[i+1][take_sum] + 1 if  dp[i+1][take_sum] else 0
                dp[i][sm] = max(take_it, dp[i+1][sm])
        
        print(dp[0][0] - 1) 
        res = []
        sum_ = 0; index = 0
        for i in range(n):
            
            # i - 1, don't take it
            no_take = dp[index + 1][sum_]
            
            # i + 1, take it + 1
            take_sum = (sum_ + digits[index]) % 3
            take_it = dp[i+1][take_sum] + 1 if  dp[i+1][take_sum] else 0
            
            if take_it >= no_take:
                res.append(digits[index])
                sum_ = take_sum
                
            index += 1  
            
        if len(res) == 0:
            return "" 
        
        if sum(res) == 0:
            return "0"
        
        return "".join(map(str, res))
