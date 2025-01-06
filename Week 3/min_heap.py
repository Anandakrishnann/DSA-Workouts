class MinHeap:
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

    # Method to return the minimum element (root of the heap)
    def get_minimum(self):
        return self.heap[0] if self.heap else None

    # Method to insert a new key into the heap
    def insert(self, data):
        self.heap.append(data)  # Add the new key to the end of the heap
        current = len(self.heap) - 1

        # Ensure the heap property is maintained by moving the element up
        while current > 0 and self.heap[current] < self.heap[self.parent(current)]:
            self.swap(current, self.parent(current))  # Swap with the parent
            current = self.parent(current)  # Move to the parent's position

    # Method to maintain the min-heap property at the given index
    def min_heapify(self, i):
        left = self.left_child(i)  # Left child index
        right = self.right_child(i)  # Right child index

        minimum = i  # Assume the current element is the minimum

        # Check if the left child is smaller than the current element
        if left < len(self.heap) and self.heap[left] < self.heap[minimum]:
            minimum = left

        # Check if the right child is smaller than the current element
        if right < len(self.heap) and self.heap[right] < self.heap[minimum]:
            minimum = right

        # If the minimum is not the current element, swap and heapify recursively
        if minimum != i:
            self.swap(i, minimum)  # Swap with the smallest child
            self.min_heapify(minimum)  # Recursively ensure the heap property

    # Method to extract (remove) the minimum element from the heap
    def extract_min(self):
        if len(self.heap) == 0:
            return None

        root = self.heap[0]  # The root is the minimum element

        # Replace the root with the last element and remove the last element
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        # Restore the min-heap property
        if len(self.heap) > 0:
            self.min_heapify(0)

        return root


# Example Usage
arr = [1, 5, 7, 3, 7, 2, 5, 8]
min_heap = MinHeap()

# Insert elements into the min-heap
for i in arr:
    min_heap.insert(i)

# Print the heap after insertion
print("Min Heap after insertion:", min_heap.heap)

# Extract (remove) the minimum element from the heap
min_heap.extract_min()

# Print the heap after extracting the minimum element
print("Min Heap after extraction:", min_heap.heap)
