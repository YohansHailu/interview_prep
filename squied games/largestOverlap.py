class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:

        res = 0
        n = len(img1)
        for di in range(-n + 1, n):
            for dj in range(-n + 1, n):


                count = 0
                for i in range(n):
                    for j in range(n):
                        if 0 <= i + di < n and 0 <= dj + j < n:
                            count += img1[i + di][j + dj] * img2[i][j]
                
                res = max(res, count)
        
        return res
