class Solution:
    def helper(self, nums, cur_perm):
        if len(nums) == 0:
            self.all_perms.append(cur_perm.copy())
        
        for i in range(len(nums)):
            cur_perm.append(nums[i])
            self.helper(nums[:i]+nums[i+1:],cur_perm)
            cur_perm.pop()
        
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.all_perms = []
        self.helper(nums, [])
        return self.all_perms
        