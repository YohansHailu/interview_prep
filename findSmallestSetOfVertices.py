class Solution:
    def find(self, node, parents):
        if node == parents[node]:
            return node
        parents[node] = self.find(parents[node], parents)
        return parents[node]
    
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        parents = {i:i for i in range(n)}
        for p, c in edges:
            parents[c] = p
        
        
        res = set()
        for node in range(n):
            res.add(self.find(node, parents))
        return res
        
