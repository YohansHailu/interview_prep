class node:
    def __init__(self):
        self.next = {}
        self.isEnd = False
    
class Solution:
    def add(self, word, root):
        cur = root
        for lt in word:
            if lt not in cur.next:
                cur.next[lt] = node()
            cur = cur.next[lt]
        cur.isEnd = True
    
    def count(self, word, root):
        if word == "":
            return 0
        
        cur = root
        for i, lt in enumerate(word):
            
            if lt not in cur.next:
                return 0
            
            cur = cur.next[lt]
            if cur.isEnd:
                ans = self.count(word[i+1:], root)
                if ans >= 1:    
                    return ans + 1
        return cur.isEnd 
            
         
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # its a trie problem
        
        # mete
        root = node()
        for word in words:
            self.add(word, root)
        
        res = []
        for word in words:
            if self.count(word, root) > 1:
                res.append(word)
                
        return res 
        
