class Solution:
    def helper(self, s, left, right):
        if s[left] != "[":
            return NestedInteger(int(s[left:right + 1]))
        if right - left == 1 and s[left] + s[right] == "[]":
            return NestedInteger()
        # if not its recuresive
        res = NestedInteger()
        left += 1
        balence = 0
        for j in range(left, right + 1):
            
            # coma and zero ballence
            if s[j] in "[":
                balence += 1

            if s[j] in "]":
                balence -= 1

            if (s[j] == "," and balence == 0) or j == right:
                res.add(self.helper(s,left, j - 1))
                left = j + 1

        return res
        # we need two pointer    

    def deserialize(self, s: str) -> NestedInteger:
        
        return self.helper(s, 0, len(s) - 1)

        



