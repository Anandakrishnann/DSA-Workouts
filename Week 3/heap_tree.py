class MinHeap:
    def __init__(self):
        self.heap = []
        
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return (i * 2) + 1
    
    def right_child(self, i):
        return (i * 2) + 1
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def get_min(self):
        return self.heap[0] if self.heap else None
    
    def size(self):
        return len(self.heap)
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def insert(self, data):
        self.heap.append(data)
        
        current = len(self.heap) - 1
        
        while current > 0 and self.heap[current] < self.heap[self.parent(current)]:
            
            self.swap(current, self.parent(current))
            current = self.parent(current)
    
    def min_heapify(self, i):
        left = self.left_child(i)
        right = self.right_child(i)
        smallest = i
        
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
            
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
            
        if smallest != i:
            self.swap(i, smallest)
            self.min_heapify(smallest)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        
        root = self.heap[0]
        
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        if len(self.heap) > 0:
            self.min_heapify(0)
        
        return root

    def decrease_key(self, i, new_value):
        if new_value > self.heap[i]:
            return "New Value is larger than the current value"
        
        self.heap[i] = new_value
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)
    
    def delete_key(self, key):
        self.decrease_key(key, float('-inf'))
        self.extract_min()
    
    def build_heap(self, arr):
        self.heap = arr
        for i in range(len(arr)//2, -1, -1):
            self.min_heapify(i)
    
    def replace_min(self, key):
        root = self.heap[0]
        self.heap[0] = key
        self.min_heapify(0)
            
        return root

    def print_heap(self):
        print(self.heap)


# Example Usage
min_heap = MinHeap()
elements = [10, 20, 5, 6, 1, 8, 12]

# Insert elements into the min-heap
for el in elements:
    min_heap.insert(el)

min_heap.print_heap()           # Print the current state of the heap
print("Minimum element:", min_heap.get_min())  # Get the minimum element
print("Extracted min:", min_heap.extract_min())  # Extract the minimum element
min_heap.print_heap()           # Print the heap after extraction
