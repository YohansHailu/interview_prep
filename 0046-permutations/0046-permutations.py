class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        all_orders = []
        
        def rec_helper(cur_order, cands):
            
            # base case
            
            if len(cands) == 0:
                all_orders.append(cur_order.copy())
                
            
            
            for cand in cands:
                
                cur_order.append(cand) # we chose it
                
                next_cands = [n_cand for n_cand in cands if n_cand != cand ]
                rec_helper(cur_order, next_cands)
                
                # we remove the previouse choice before we go to the next choice
                cur_order.pop()
        
        rec_helper([], nums)
        
        return all_orders
                
            
            