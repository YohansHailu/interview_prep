class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # the maximam so far will be used 
        
        # tath index 
        used_bricks = [] 
        
        for i in range(1, len(heights)):
            needed_bricks = heights[i] - heights[i-1]
            if needed_bricks > 0:
                heappush(used_bricks, -1*needed_bricks)
                bricks -= needed_bricks
            
            if bricks < 0 and ladders and used_bricks:
                new_bricks = -1* heappop(used_bricks)
                bricks += new_bricks
                ladders -= 1
                
            if bricks < 0:
                return i-1
            
        return len(heights) - 1
                
