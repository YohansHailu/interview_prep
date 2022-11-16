class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        for i in range(len(nums) - 2):
            c,b,a = nums[i:i+3]
            if a+b > c:
                return a + b + c
        return 0
