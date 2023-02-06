class Solution:
    def dfs_helper(self, graph, cur, visited):
        visited.add(cur) 
        res = 0
        for nbr in graph[cur]:
            if nbr  not in visited:
                res = max(res, self.dfs_helper(graph, nbr, visited))
        return res + 1
            
    def longestStrChain(self, words: List[str]) -> int:
        graph = {word:[] for word in words}
        for word in words:
            for i in range(len(word)):
                p = word[:i] + word[i+1:]
                if p in graph: graph[p].append(word)
        
        res = 0
        for word in words:
            visited = set()
            res = max(res, self.dfs_helper(graph, word, visited))
        return res
