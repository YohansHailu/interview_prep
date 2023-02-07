class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # lets keep k size max heap
        minheap = [i for i in nums[:k]]
        heapify(minheap)
        
        for i in nums[k:]:
            heappushpop(minheap,i)
        
        return heappop(minheap)
        
        
