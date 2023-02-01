class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:

        prefix = [row.copy() for row in mat]
        for row in prefix:
            for i in range(1, len(row)):
                row[i] += row[i - 1]
        

        n,m = len(mat), len(mat[0])
        answer = [[0]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                
                top = max(0, i - k)
                bottom = min(i + k, n - 1)

                for x in range(top, bottom + 1):
                    
                    prefix_row = prefix[x]

                    right_end = min(m-1, j + k)
                    left_end = max(0, j - k)
                    answer[i][j] += prefix_row[right_end] - (prefix_row[left_end - 1] if left_end else 0)
        
        return answer
