class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:

        # you plant the logest first

        # or you see the sum

        # you see the order 

        work = list(zip(plantTime, growTime))

        work.sort(key = lambda x: x[1])

        work.reverse()
        offset = 0
        res = 0
        for plant, grow in work:
            total = plant + grow + offset
            res = max(res, total)
            offset += plant
        
        return res
