class Solution:
    def dfs(self, cur, end, cost,graph, visited):
        
        if cur == end:
            return cost
        
        visited.add(cur)
        
        for nbr, weight in graph[cur]:
            
            if nbr in visited:
                continue
                
            res = self.dfs(nbr, end, cost*weight, graph, visited)
            
            if res != -1:
                return res
            
        return -1 
            
        
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        #make graph
        graph = {}
        
        i = 0
        for start, end in equations:
            
            if start not in graph:
                graph[start] = []
                
            if end not in graph:    
                graph[end] = []
                
            graph[start].append((end, values[i]))
            graph[end].append((start, 1/values[i]))
            i += 1
         
        ans = []
        for start, end in queries:
            if start not in graph:    
                ans.append(-1)
                continue
                
            ans.append(self.dfs(start, end, 1, graph, set() ) )
        
        return ans
