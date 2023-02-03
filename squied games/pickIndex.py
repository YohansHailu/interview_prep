class Solution:

    def __init__(self, w: List[int]):

        # we random number generator
        # generats 0, w-1

        # ignor its and not egnor
        # paly with ranger make w times greater than the other

        # 10^4* 10^5 --> 10**9
        
        # ------------------------ 10**9

        # 0 -- 1 1--4

        # then binary search 

        # thats it
        self.prefix = w
        for i in range(1, len(w)):
            self.prefix[i] += self.prefix[i-1]

    def pickIndex(self) -> int:
        rand_val = randint(1, self.prefix[-1])

        # [1,1,100] # [1,2,102]
        return bisect_left(self.prefix, rand_val)

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
