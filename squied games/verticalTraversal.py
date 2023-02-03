class Solution:
    def dfs(self, root, position, col_map):
        if root == None:
            return
        i,j = position 
        
        col_map[j].append([i, root.val])
        self.dfs(root.left, (i+1, j-1), col_map)
        self.dfs(root.right, (i+1, j+1), col_map)
        
        
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        col_map = defaultdict(list)
        self.dfs(root, (0, 0), col_map) # side efficet
        
        res = []
        for col in sorted(col_map.keys()):
            col_arr = col_map[col]
            col_arr.sort()
            res.append([val for i,val in col_arr])
        return res
