
class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        max_i = [0]*len(nums)

        cur = len(nums) - 1
        for i in range(len(nums))[::-1]:
            if nums[i] > nums[cur]:
                cur = i
            max_i[i] = cur
        
        for i in range(len(nums)):
            if nums[i] != nums[max_i[i]]:
                nums[i], nums[max_i[i]] = nums[max_i[i]], nums[i]
                break

        return int("".join(nums))
