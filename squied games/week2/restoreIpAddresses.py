class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        res = []
        def dp(i, path):


            if i >= len(s):
                if len(path) == 4:
                    res.append(path.copy())
                return
            
            if len(path) >= 4:
                return 0

            if i+1 <= len(s):
                path.append(s[i:i+1])
                dp(i+1, path)
                path.pop()

            if s[i] != "0" and i + 2 <= len(s):
                path.append(s[i:i+2])
                dp(i+2, path)
                path.pop()

            if s[i] != "0" and i + 3 <= len(s) and int(s[i:i+3]) <=  255:
                path.append(s[i:i+3])
                dp(i+3, path)
                path.pop()
            
        dp(0, [])
        return [".".join(row) for row in res]
