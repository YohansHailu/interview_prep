class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        # minimam B in k window

        res = inf
        for i in range(len(blocks) - k + 1):

            res = min(res, blocks[i:i+k].count("W"))
        
        return res
