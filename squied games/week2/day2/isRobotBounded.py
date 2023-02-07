class Solution:
    def isRobotBounded(self, word: str) -> bool:

        cur = (0,0)
        dirs = [(0,1),(-1,0), (0,-1),(1,0)]

        memo = set()
        i = 0
        d = 0
        for _ in range(10**5):
            state = (cur, i, d)
            if state in memo:
                return True
            memo.add(state)
            
            i += 1
            i %= len(word)

            if word[i] == "G":
                cur = (cur[0] + dirs[d][0], cur[1] + dirs[d][1])

            if word[i] == "L":
                d += 1
                d %= len(dirs)
            if word[i] == "R":
                d -= 1
                if d < 0:
                    d = len(dirs) - 1

        return False
