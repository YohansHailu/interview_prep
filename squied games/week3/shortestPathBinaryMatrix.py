class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        m = len(grid) 
        n = len(grid[0]) 
        que = deque()
        que.append((0,0))
        visited = set() 
        
        level = 1
        while que:
            for _ in range(len(que)):
                cur = que.popleft()
                  
                if cur == (m-1, n-1):
                    return level
                
                for xi, xj in [(1,1),(1,-1),(-1,1),(-1,-1),(0,1),(0,-1),(1,0),(-1,0)]:
                    i,j = cur
                    ni = i + xi
                    nj = j + xj
                    if not (0 <= ni < m and 0 <= nj < n):
                        continue
                    if grid[ni][nj] == 1:
                        continue
                    if (ni,nj) in visited:
                        continue
                    
                    que.append((ni,nj))
                    visited.add((ni,nj))
                    
            level += 1    
        return -1  
