class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        changed.sort()
        if len(changed)%2:
            return []
        
        d = dict()
        for elt in changed:
            if elt in d:
                d[elt]+=1
            else:
                d[elt] = 1
               
        org_arr = []
        for i in range(len(changed)):
            if changed[i] == 0:
                d[0] -=1
            
            
            twI = 2*changed[i]
            if twI in d and d[twI]>0 and d[changed[i]] > 0:
                org_arr.append(changed[i])
                d[twI]-=1
            
            if changed[i] != 0:    
                d[changed[i]]-=1
        
                             
        if len(changed)/2 == len(org_arr):
            return org_arr
        
        return []
