class Solution:
    def join(self, line, maxWidth, chars_count, is_last):
        totalSpace = maxWidth - chars_count 
        
        betweenSpace = 0
        if len(line) > 1:
            betweenSpace = totalSpace// (len(line) - 1)
            
        if is_last:
            betweenSpace = 1
            
        extraSpace = totalSpace - betweenSpace * (len(line) - 1)
        if is_last: 
            return (betweenSpace*" ").join(line) + " "*extraSpace
        
        res = [line[0]]
        for i in range(1, len(line)):
            space = " "*betweenSpace
            if extraSpace:
                space += " "
                extraSpace -= 1
            res.append(space + line[i])
        return "".join(res) + " "*extraSpace
    
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line = []
        chars_count = 0 
        for word in words:
            cur_width = chars_count + len(line) - 1
            can_fit = cur_width + len(word) + 1 <= maxWidth
            
            if not can_fit:
                res.append(self.join(line, maxWidth, chars_count, False))
                line = []
                chars_count  = 0
                
            line.append(word)
            chars_count  += len(word)
            
        res.append(self.join(line, maxWidth, chars_count, True))
        return res
