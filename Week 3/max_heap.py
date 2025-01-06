class MaxHeap:
    def __init__(self):
        self.heap = []  # Initialize an empty list to represent the heap
    
    # Method to find the index of the parent of the node at index i
    def parent(self, i):
        return (i - 1) // 2
    
    # Method to find the index of the left child of the node at index i
    def left_child(self, i):
        return (i * 2) + 1
    
    # Method to find the index of the right child of the node at index i
    def right_child(self, i):
        return (i * 2) + 2
    
    # Method to swap two elements in the heap
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    # Method to return the length of the heap
    def length(self):
        return len(self.heap)
    
    # Method to return the maximum element (root of the heap)
    def get_max(self):
        return self.heap[0] if self.heap else None
    
    # Method to insert a new key into the heap
    def insert(self, key):
        self.heap.append(key)  # Add the new key to the end of the heap
        
        # Ensure the heap property is maintained by moving the element up
        current = self.length() - 1
        
        while current > 0 and self.heap[current] > self.heap[self.parent(current)]:
            self.swap(current, self.parent(current))  # Swap with the parent
            current = self.parent(current)  # Move to the parent's position
    
    # Method to maintain the max-heap property at the given index
    def max_heapify(self, i):
        left = self.left_child(i)  # Left child index
        right = self.right_child(i)  # Right child index
        
        largest = i  # Assume the current element is the largest
        
        # Check if the left child is larger than the current element
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        
        # Check if the right child is larger than the current element
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        
        # If the largest is not the current element, swap and heapify recursively
        if largest != i:
            self.swap(i, largest)  # Swap with the largest child
            self.max_heapify(largest)  # Recursively ensure the heap property
    
    # Method to extract (remove) the maximum element from the heap
    def extract_max(self):
        if len(self.heap) == 0:
            return None
        
        root = self.heap[0]  # The root is the maximum element
        
        # Replace the root with the last element and remove the last element
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        # Restore the max-heap property
        if len(self.heap) > 0:
            self.max_heapify(0)
        
        return root
    
    # Method to increase the key at index i to a new value
    def increase_key(self, i, new_value):
        self.heap[i] = new_value  # Set the new value
        
        # Move the element up the heap until the max-heap property is restored
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)
    
    # Method to delete a key at a given index
    def delete_key(self, key):
        if 0 <= key < self.length():
            self.increase_key(key, float('inf'))  # Increase the key to infinity
            
            self.extract_max()  # Remove the maximum element (which is the key)
    
    # Method to perform heap sort on the heap
    def heap_sort(self):
        sorted_array = []
        
        # Repeatedly extract the maximum element to build a sorted array
        while self.length() > 0:
            sorted_array.append(self.extract_max())
        
        return sorted_array
    
    # Method to build a max heap from an unsorted array
    def build_max_heap(self, arr):
        self.heap = arr  # Set the heap to the given array
        n = len(self.heap)
        
        # Start from the last non-leaf node and heapify all nodes
        for i in range(n // 2 - 1, -1, -1):
            self.max_heapify(i)
    
    # Method to replace the maximum element with a new value
    def replace_max(self, new_val):
        root = self.heap[0]  # Store the current maximum
        
        self.heap[0] = new_val  # Replace the root with the new value
        
        self.max_heapify(0)  # Restore the heap property
        
        return root  # Return the old maximum value


# Example Usage
max_heap = MaxHeap()

# Insert elements into the max-heap
elements = [10, 20, 5, 6, 1, 8, 12]
for el in elements:
    max_heap.insert(el)

# Print the heap after insertion
print("Max Heap after insertion:", max_heap.heap)  # Print the current state of the heap

# Get the maximum element
print("Maximum element:", max_heap.get_max())

# Extract (remove) the maximum element from the heap
print("Extracted max:", max_heap.extract_max())

# Print the heap after extraction
print("Max Heap after extraction:", max_heap.heap)

# Increase the key at index 2 to 25
max_heap.increase_key(2, 25)
print("Max Heap after increasing key at index 2 to 25:", max_heap.heap)

# Delete the key at index 3
max_heap.delete_key(3)
print("Max Heap after deleting key at index 3:", max_heap.heap)

# Perform heap sort and print the sorted array
sorted_array = max_heap.heap_sort()
print("Sorted array:", sorted_array)
