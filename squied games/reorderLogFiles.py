
# the first word is identifier

# the digit-logs will stay the same

# the letter logs should be sorted lexographically
    # if equal they should be sorted by there identifier

# constraint is just 100 by 100

# sperates the 


# its only a digit
# its only a letter
class Solution:
    def get_log_identifier(self, line):
        index = line.find(" ")
        return (line[index +1:] , line[:index])
    
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs = []
        letter_logs = []
        for log in logs:
            space = " "
            index = log.find(space)
            if log[index + 1].isnumeric():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        
        letter_logs.sort(key = lambda log:self.get_log_identifier(log))
        
        return letter_logs + digit_logs
        
