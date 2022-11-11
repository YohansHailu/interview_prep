class Solution:
    def top_sort(self, nodes, graph):
        # indegree
        res = []
        indegree = defaultdict(int) 
        for node in nodes:
            for nbr in graph[node]:
                if nbr in nodes:
                    indegree[nbr] += 1
        
        que = deque([node for node in nodes if indegree[node] == 0])
        
        res = []
        while que:
            cur = que.pop()
            res.append(cur)
                
            for nbr in graph[cur]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0 and nbr in nodes:
                    que.append(nbr)
                    
        if len(res) < len(nodes):
            return []
        
        return res 
        
    def sortItems(self, n: int, m: int, group: List[int], graph: List[List[int]]) -> List[int]:
        
        # preprocces the groups
        for i in range(len(group)):
            if group[i] == -1:
                group[i] = m
                m += 1
        
        group_nodes = defaultdict(list)
        new_group = m
        for node,val in enumerate(group):
            group_nodes[val].append(node)
            
        group_graph = defaultdict(set)
        for node in range(n):
            for nbr in graph[node]:
                a = group[node]
                b = group[nbr]
                if a != b:
                    group_graph[a].add(b)
                    
        sorted_groups = self.top_sort(set(range(m)), group_graph)
        res = []
        for group_id in sorted_groups:
            nodes = group_nodes[group_id]
            sorted_nodes = self.top_sort(nodes, graph)
            
            if len(sorted_nodes) < len(nodes):
                return [] 
            
            for node in sorted_nodes:
                res.append(node)
                
        return res[::-1]
