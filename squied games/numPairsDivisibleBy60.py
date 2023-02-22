class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        history = defaultdict(int) 
        res = 0
        for val in time:
            for hval in history:
                if (hval + val) % 60 == 0:
                    res += history[hval]
            history[val] += 1
        return res 
