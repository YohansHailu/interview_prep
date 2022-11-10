class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        
        n = len(colors)
        graph = [[] for _ in range(n)] 
        indegree = [0]*n
        for a,b  in edges:
            graph[a].append(b)
            indegree[b] += 1
            
        
        que = deque([node for node in range(n) if indegree[node] == 0])
        
        node_freq = [defaultdict(int) for _ in range(n)] 
        
        for node, color in enumerate(colors):
            node_freq[node][color] += 1
            
        count = 0 
        
        res = -1 
        while que:
            cur = que.popleft()
            count += 1
            # count if no nbr 
            
            path_freq = node_freq[cur]
            for color in path_freq:
                res = max(res, path_freq[color])
            
            for nbr in graph[cur]:
                # combin 
                nbr_color = colors[nbr]
                path_freq[nbr_color] += 1
                
                nbr_freq = node_freq[nbr]
                for color in path_freq:
                    nbr_freq[color] = max(nbr_freq[color], path_freq[color])
                    
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    que.append(nbr)
                    
                path_freq[nbr_color] -= 1
                
        if count < n:        
            return -1
        
        return res 
