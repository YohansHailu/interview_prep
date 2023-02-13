class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cur = 0
        before = defaultdict(int)
        before[0] = 1
        res = 0
        for val in nums:
            cur += val
            cur %= k
            # a = (b - k)%
            a = (cur - k)%k
            res += before[a]
            before[cur] += 1
            
        return res
