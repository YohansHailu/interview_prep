class node:
    def __init__(self, key, val, next = None, prev = None):
        self.key = key
        self.val = val
        self.prev = prev 
        self.next = next
        
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_count = 0
        
        self.rear = node(0,0)
        self.front = node(0,0)
        
        self.rear.next = self.front
        self.front.prev = self.rear
        
        self.linked_dict = {}
        
    def get(self, key: int) -> int:
        if key not in self.linked_dict:
            return -1
        
        node = self.linked_dict[key]
        # delelte it
        pre_of_node = node.prev 
        next_of_node = node.next
        
        pre_of_node.next = next_of_node
        next_of_node.prev = pre_of_node
        
        # put it to front
        self.put_node_to_front(node)
        
        return node.val
        
        
        return node.val
    
    def put_node_to_front(self, node):
        
        front_prev = self.front.prev 
        
        node.next = self.front
        node.prev = front_prev  
        
        self.front.prev = node
        front_prev.next = node
        
        
    def delete_from_rear(self):
        
        deleted_node = self.rear.next
        self.rear.next = deleted_node.next
        self.rear.next.prev = self.rear
        
        del self.linked_dict[deleted_node.key]
        self.node_count -= 1
        
        
    def add_new_node(self, key, val):
        if self.node_count == self.capacity:
            self.delete_from_rear()
            
        new_node = node(key, val)
        self.put_node_to_front(new_node)
        self.linked_dict[key] = new_node
        self.node_count += 1
        
    def put(self, key: int, value: int) -> None:
        if key in self.linked_dict:
            self.linked_dict[key].val = value
            self.get(key)
            return
        
        self.add_new_node(key, value) 
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
