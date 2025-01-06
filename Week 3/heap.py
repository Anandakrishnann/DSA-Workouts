class MinHeap:
    def __init__(self):
        self.heap = []
        
    
    def insert(self, val):
        self.heap.append(val)
        self._heapify_up( len(self.heap) - 1 )
    
    def _heapify_up(self, index):
        parent_index = ( index - 1 ) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self._swap(index, parent_index)
            self._heapify_up(parent_index)
            
    
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    
    def remove(self):
        if len(self.heap) > 1:
            self._swap(0, len(self.heap) - 1 )
            min_value = self.heap.pop()
            
    
    def _heapify_down(self, index):
        
        smallest = index
        
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        
        