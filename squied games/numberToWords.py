class Solution:
    get_string =  {
        1 : " One",
        2 : " Two",
        3 : " Three",
        4 : " Four",
        5 : " Five",
        6 : " Six",
        7 : " Seven",
        8 : " Eight",
        9 : " Nine",
        10 : " Ten",
        11 : " Eleven",
        12 : " Twelve",
        13 : " Thirteen",
        14 : " Fourteen",
        15 : " Fifteen",
        16 : " Sixteen",
        17 : " Seventeen",
        18 : " Eighteen",
        19 : " Nineteen",
        20 : " Twenty",
        30 : " Thirty",
        40 : " Forty",
        50 : " Fifty",
        60 : " Sixty",
        70 : " Seventy",
        80 : " Eighty",
        90 : " Ninety",
        
        }
    Hundred  = 10**2
    Thousand = 10**3 
    Million = 10**6
    Billion = 10**9
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        return self.helper(num).strip();
    def helper(self, num: int) -> str:
        if num == 0:
            return ""
        
        if num <= 20:
            return self.get_string[num]
        elif num < 100:
            if num%10 == 0:
                return self.get_string[num]
            else:
                return self.helper( (num//10) * 10) + self.helper(num%10)
        
        elif num < self.Thousand:
            return self.helper(num//self.Hundred) + " Hundred" + self.helper(num%self.Hundred)
        elif num < self.Million:
            return self.helper(num//self.Thousand) + " Thousand" + self.helper(num%self.Thousand)
        elif num < self.Billion:
            return self.helper(num//self.Million) + " Million" + self.helper(num%self.Million)
        else:
            return self.helper(num//self.Billion) + " Billion" + self.helper(num%self.Billion)
        
            
                                          
                
