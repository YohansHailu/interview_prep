# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursive_helper(self, left, right, nums):
            # base case
            if left > right:
                return None
            
            mid = (left + right)//2 
            
            cur_node = TreeNode(nums[mid])
            
            left_sub_tree = self.recursive_helper(left, mid - 1, nums)
            right_sub_tree = self.recursive_helper(mid + 1, right, nums)
            
            cur_node.left = left_sub_tree
            cur_node.right = right_sub_tree
            
            return cur_node
        
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        
        left = 0
        right = len(nums) - 1
        return self.recursive_helper(left, right, nums)