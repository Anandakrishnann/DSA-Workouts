from collections import deque

# class HasMap:
#     def __init__(self,size=10):
#         self.size = size
#         self.table = [[]for _ in range(size)]
        
#     def has_function(self,key):
#         return hash(key)%self.size
    
#     def insert(self,key,val):
#         index = self.has_function(key)
#         bucket = self.table[index]
        
#         for i in bucket:
#             if i[0] == key:
#                 i[1] = val
#                 return 
            
#         bucket.append([key, val])
        
#     def retrieve(self, key):
#         index = self.has_function(key)
#         bucket = self.table[index]
        
#         for i, kv in enumerate(bucket):
#             k,v = kv
#             if k == key:
#                 return v
#         return None
    
#     def delete(self,key):
#         index = self.has_function(key)
#         bucket = self.table[index]
        
#         for i , kv in enumerate(bucket):
#             k,v = kv
#             if k == key:
#                 del bucket[i]
#                 return True
#         return False
    
#     def display(self):
#         for i, value in enumerate(self.table):
#             print(f"{i}:{value}")
            
            
            
# ht = HasMap()

# ht.insert("apple", 10)
# ht.insert("banana", 20)
# ht.insert("grape", 30)
# ht.insert("orange", 40)
# ht.insert("orange", 60)

# print("retrieve",ht.retrieve("apple"))

# print("delete",ht.delete("apple"))

# ht.display()    

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# def merge_sort(arr):
#     if len(arr) >1:
        
#         mid = len(arr)//2
        
#         left_half = arr[:mid]
#         right_half = arr[mid:]
        
#         merge_sort(left_half)
#         merge_sort(right_half)
        
#         i = j = k = 0
        
#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]
#                 i += 1
#             else:
#                 arr[k] = right_half[j]
#                 j += 1
            
#             k += 1
        
#         while i < len(left_half):
#             arr[k] = left_half[i]
            
#             i += 1
#             k += 1
        
#         while j < len(right_half):
#             arr[k] = right_half[j]
            
#             j += 1
#             k += 1

# arr = [1,8,2,7,3,6,4,5]
# merge_sort(arr)
# print(arr)


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# def partition(arr, low, high):
#     mid = (low+high) // 2
#     pivot = arr[mid]
    
#     arr[mid],arr[high] = arr[high],arr[mid]
    
#     i = low-1
    
#     for j in range(low,high):
#         if arr[j] < pivot:
#             i += 1
#             arr[i],arr[j] = arr[j],arr[i]
    
#     arr[i+1],arr[high] = arr[high],arr[i+1]
#     return i + 1


# def quick_sort(arr, low, high):
    
#     if low < high:
#         pi = partition(arr, low, high)
        
#         quick_sort(arr, low, pi-1)
#         quick_sort(arr, pi+1, high)
        

# arr = [1,8,2,7,3,6,4,5]
# n = len(arr)
# quick_sort(arr, 0, n-1)
# print(arr)


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# class Stack:
#     def __init__(self):
#         self.stack = []
        
#     def push(self,data):
#         self.stack.append(data)
        
#     def list_to_stack(self,data):
#         for i in data:
#             self.push(i)
    
#     def pop(self):
#         return self.stack.pop()
    
#     def is_empty(self):
#         return len(self.stack) == 0
    
#     def display(self):
#         print(self.stack)
        

# def string_reverse(data):
#     stack = Stack()
    
#     for i in data:
#         stack.push(i)
    
#     res = ""
#     while not stack.is_empty():
#         res += stack.pop()
    
#     return res

# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)

# arr = [5,6,7,8,9,10]

# stack.list_to_stack(arr)

# stack.pop()
# print(stack.is_empty())
# stack.display()

# string = "gnirts"

# res = string_reverse(string)
# print(res)


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



# class Queue:
#     def __init__(self):
#         self.queue = []
    
#     def enqueue(self,data):
#         self.queue.append(data)
        
#     def dequeue(self):
#         self.queue.pop(0)

#     def peek(self):
#       if not self.is_empty():
#           return self.queue[0]
#       else:
#           return  "Queue is empty"
    
#     def is_empty(self):
#         return len(self.queue) == 0
    
#     def display(self):
#         print(self.queue)
        

# queue = Queue()

# queue.enqueue(0)
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# queue.enqueue(4)
# queue.enqueue(5)
# queue.dequeue()
# queue.peak()

# print(queue.is_empty())
# queue.display()


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# class QueueUsingStack:
#     def __init__(self):
#         self.stack1 = []
#         self.stack2 = []
    
#     def enqueue(self,data):
#         self.stack1.append(data)
        
#     def dequeue(self):
#         if not self.stack2:
            
#             while self.stack1:
#                 self.stack2.append(self.stack1.pop())
        
#         if not self.stack2:
#             print("Queue is empty")
#             return None

#         print(self.stack1)
#         print(self.stack2)
#         return self.stack2.pop()
    
#     def peek(self):
#         if not self.stack2:
#             while self.stack1:
#                 self.stack2.append(self.stack1.pop())
            
#         if not self.stack2:
#             print("Queue is empty")
#             return None
        
#         return self.stack2[-1]
    
#     def is_empty(self):
#         return len(self.stack1) == 0 and len(self.stack2) == 0
    

# queue = QueueUsingStack()
# queue.enqueue(1)
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# queue.enqueue(4)
# queue.dequeue()
# queue.peek()
# queue.is_empty()


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# class StackUsingQueue:
#     def __init__(self):
#         self.queue1 = []
#         self.queue2 = []
    
#     def push(self,data):
#         self.queue2.append(data)
        
#         while self.queue1:
#             self.queue2.append(self.queue1.pop(0))
        
#         self.queue1, self.queue2 = self.queue2,self.queue1
        
    
#     def pop(self):
#         if len(self.queue1) == 0:
#             return None
#         return self.queue1.pop(0)
    
#     def top(self):
#         if len(self.queue1) == 0:
#             return None
        
#         return self.queue1[0]
    
#     def is_empty(self):
#         return len(self.queue1) == 0
    
#     def display(self):
#         print(self.queue1)

# queue = StackUsingQueue()
# queue.push(1)
# queue.push(2)
# queue.push(3)
# queue.push(4)
# queue.push(5)

# print(queue.pop())

# print(queue.top())

# print(queue.is_empty())

# print(queue.display())


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i -1
#         while j >= 0 and key < arr[j]:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = key
        
#     return arr

# arr = [3,5,9,7,5,3,8,6,655,34]
# insertion_sort(arr)
# print(arr)



# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# def bubble_sort(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr)-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
                
#     return arr


# arr = [3,5,9,7,5,3,8,6,655,34]
# bubble_sort(arr)
# print(arr)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# class MinHeap:
#     def __init__(self):
#         self.heap = []
    
#     def parent(self, i):
#         return (i - 1) // 2
    
#     def left_child(self, i):
#         return 2 * i + 1
    
#     def right_child(self, i):
#         return 2 * i + 2
    
#     def insert(self, key):
#         # Insert the new key at the end of the heap
#         self.heap.append(key)
#         # Heapify up to maintain heap property
#         current = len(self.heap) - 1
#         print(f'current is {current}')
#         print(f'the parent is {self.parent(current)}')
        
#         # Heapify up: Compare with parent and swap if necessary
#         while current > 0 and self.heap[current] < self.heap[self.parent(current)]:
            
#             self.swap(current, self.parent(current))
#             current = self.parent(current)
    
#     def min_heapify(self, i):
#         left = self.left_child(i)
#         right = self.right_child(i)
#         smallest = i
        
#         # Find the smallest among the node and its children
#         if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
#             smallest = left
        
#         if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
#             smallest = right
        
#         # Swap and continue heapifying if root is not the smallest
#         if smallest != i:
#             self.swap(i, smallest)
#             self.min_heapify(smallest)
    
#     def extract_min(self):
#         if len(self.heap) == 0:
#             return None
        
#         # The root is the minimum element
#         root = self.heap[0]
        
#         # Move the last element to the root and pop the last element
#         self.heap[0] = self.heap[-1]
#         self.heap.pop()
        
#         # Heapify down to maintain heap property
#         if len(self.heap) > 0:
#             self.min_heapify(0)
        
#         return root
    
#     def swap(self, i, j):
#         self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
#     def get_min(self):
#         return self.heap[0] if self.heap else None
    
#     def print_heap(self):
#         print(self.heap)
    
# # Example Usage
# min_heap = MinHeap()
# elements = [10, 20, 5, 6, 1, 8, 12]

# # Insert elements into the min-heap
# for el in elements:
#     min_heap.insert(el)

# min_heap.print_heap()           # Print the current state of the heap
# print("Minimum element:", min_heap.get_min())  # Get the minimum element
# print("Extracted min:", min_heap.extract_min())  # Extract the minimum element
# min_heap.print_heap()           # Print the heap after extraction



# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



# class BinarySearchTree:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
    
#     def add_child(self, data):
#         if data == self.data:
#             return 
        
#         if data < self.data:
#             if self.left:
#                 self.left.add_child(data)
#             else:
#                 self.left = BinarySearchTree(data)
#         else:
#             if self.right:
#                 self.right.add_child(data)
#             else:
#                 self.right = BinarySearchTree(data)
    
#     def find_maximum(self):
#         if self.right is None:
#             return self.data
#         return self.right.find_maximum()
    
#     def find_minimum(self):
#         if self.left is None:
#             return self.data
#         return self.left.find_minimum()
    
#     def find_left_count(self):
#         if self.left is None:
#             return 0
#         return 1 + self.left.find_left_count()
    
#     def find_right_count(self):
#         if self.right is None:
#             return 0 
#         return 1 + self.right.find_right_count()
    
#     def in_order_traversal(self):
#         element = []
#         if self.left:
#             element += self.left.in_order_traversal()
#         element.append(self.data)
#         if self.right:
#             element += self.right.in_order_traversal()
#         return element
    
#     def post_order_traversal(self):
#         element = []
#         if self.left:
#             element += self.left.post_order_traversal()
#         if self.right:
#             element += self.right.post_order_traversal()
#         element.append(self.data)
#         return element
    
#     def pre_order_traversal(self):
#         element = [self.data]
#         if self.left:
#             element += self.left.pre_order_traversal()
#         if self.right:
#             element += self.right.pre_order_traversal()
#         return element
    
#     def search(self, val):
#         if val == self.data:
#             return True
#         if val < self.data:
#             if self.left:
#                 return self.left.search(val)
#             else:
#                 return False
#         if val > self.data:
#             if self.right:
#                 return self.right.search(val)
#             else:
#                 return False
    
#     def delete(self, val):
#         if val < self.data:
#             if self.left:
#                 self.left = self.left.delete(val)
                
#         elif val > self.data:
#             if self.right:
#                 self.right = self.right.delete(val)
                
#         else:
#             if self.left and self.right is None:
#                 return None
            
#             if self.left is None:
#                 return self.right
            
#             if self.right is None:
#                 return self.left
            
#             min_val = self.right.find_minimum()
#             self.data = min_val
#             self.right = self.right.delete(min_val)
            
#         return self
            
# def is_bst(node, min_val=float('-inf'), max_val=float('inf')):
#     if node is None:
#         return True
#     if not(min_val < node.data < max_val):
#         return False
#     return (is_bst(node.left, min_val, node.data)) and (is_bst(node.right, node.data, max_val))
    
# def build_tree(arr):
#     root = BinarySearchTree(arr[0])
#     for i in range(1, len(arr)):
#         root.add_child(arr[i])
#     return root

# if __name__ == '__main__':
#     numbers = [23, 4, 23, 66, 63, 12, 674, 12, 2]
#     number_tree = build_tree(numbers)
    
#     # Count left and right nodes
#     left_count = number_tree.find_left_count()
#     right_count = number_tree.find_right_count()

#     print("Left subtree node count:", left_count)
#     print("Right subtree node count:", right_count)
#     print(number_tree.search(660))



# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




# class MaxHeap:
#     def __init__(self):
#         self.heap = []
        
#     def parent(self, i):
#         return (i -1)//2
    
#     def left_child(self, i):
#         return (i * 2) + 1
    
#     def right_child(self, i):
#         return (i * 2) + 2
    
#     def swap(self, i, j):
#         self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
#     def get_max(self):
#         return self.heap[0] if self.heap else None
    
#     def extract_max(self):
#         if len(self.heap) == 0:
#             return None
        
#         root = self.heap[0]
#         self.heap[0] = self.heap[-1]
        
#         if len(self.heap) > 0:
#             self.max_heapify(0)
            
#         return root
    
#     def max_heapify(self, data):
#         left = self.left_child(data)
#         right = self.right_child(data)
        
#         largest = data
        
#         if left < len(self.heap) and self.heap[left] > self.heap[largest]:
#             largest = left
            
#         if right < len(self.heap) and self.heap[right] > self.heap[largest]:
#             largest = right
        
#         if largest != data:
#             self.swap(data, largest)
#             self.max_heapify(largest)
            
#     def insert(self, data):
#         self.heap.append(data)
#         current = len(self.heap) - 1
        
#         while current > 0 and self.heap[current] > self.heap[self.parent(current)]:
#             self.swap(current, self.parent(current))
#             current = self.parent(current)
    
#     def increase_key(self, i, value):
#         self.heap[i] = value
        
#         while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
#             self.swap(i, self.parent(i))
#             i = self.parent(i)
    
#     def delete_key(self, key):
#         if 0 <= key < len(self.heap):
#             self.increase_key(key, float('inf'))
#             self.extract_max()
    
#     def replace_max(self, key):
#         root = self.heap[0]
        
#         self.heap[0] = key
#         self.max_heapify(0)
        
#         return root
    
#     def heap_sort(self):
#         sorted_array = []
#         while len(self.heap) > 0:
#             sorted_array.append(self.extract_max())
#         return sorted_array



# # Example Usage
# max_heap = MaxHeap()

# # Insert elements into the max-heap
# elements = [10, 20, 5, 6, 1, 8, 12]
# for el in elements:
#     max_heap.insert(el)

# print("Max Heap after insertion:", max_heap.heap)  # Print the current state of the heap
# print("Maximum element:", max_heap.get_max())  # Get the maximum element
# print("Extracted max:", max_heap.extract_max())  # Extract the maximum element
# print("Max Heap after extraction:", max_heap.heap)  # Print the heap after extraction

# # Increase key operation
# max_heap.increase_key(2, 25)
# print("Max Heap after increasing key at index 2 to 25:", max_heap.heap)

# # Delete key operation
# max_heap.delete_key(3)  # Delete the key at index 3
# print("Max Heap after deleting key at index 3:", max_heap.heap)

# # Heap sort operation
# sorted_array = max_heap.heap_sort()
# print("Sorted array:", sorted_array)  # Print the sorted array


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



# class BinarySearchTree:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

#     def add_child(self, data):
#         if data == self.data:
#             return 
        
#         if data < self.data:
#             if self.left:
#                 self.left.add_child(data)
#             else:
#                 self.left = BinarySearchTree(data)
#         else:
#             if self.right:
#                 self.right.add_child(data)
#             else:
#                 self.right = BinarySearchTree(data)

#     # Helper function to find the maximum value in a subtree
#     def find_max(self, node):
#         current = node
#         while current.right:
#             current = current.right
#         return current.data

#     # Function to find the second largest node
#     def find_second_largest(self, node=None):
#         if node is None:
#             node = self
        
#         # If there's no right subtree, the second largest is the largest in the left subtree
#         if node.right is None and node.left is not None:
#             return self.find_max(node.left)
        
#         # If the right child has no children, the current node is the second largest
#         if node.right and not node.right.right and not node.right.left:
#             return node.data

#         # Recur down the right subtree to find the largest node
#         return self.find_second_largest(node.right)

# # Example usage
# if __name__ == '__main__':
#     numbers = [23, 4, 66, 12, 63, 674, 2]
#     number_tree = BinarySearchTree(numbers[0])
#     for num in numbers[1:]:
#         number_tree.add_child(num)

#     print("Second largest:", number_tree.find_second_largest())

# class MHeap:
#     def __init__(self):
#         self.heap = []

#     def parent(self, i):
#         return (i - 1) // 2
    
#     def left_child(self, i):
#         return (i * 2) + 1
    
#     def right_child(self, i):
#         return (i * 2) + 2
    
#     def swap(self, i, j):
#         self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
#     def insert(self, data):
#         self.heap.append(data)
        
#         current = len(self.heap) - 1
        
#         while current > 0 and self.heap[current] > self.heap[self.parent(current)]:
#             self.swap(current, self.parent(current))
#             current = self.parent(current)
    
#     def max_heapify(self, i):
#         left = self.left_child(i)
#         right = self.right_child(i)
        
#         largest = i
        
#         if left < len(self.heap) and self.heap[left] > self.heap[largest]:
#             largest = left
        
#         if right < len(self.heap) and self.heap[right] > self.heap[largest]:
#             largest = right
        
#         if largest != i:
#             self.swap(i, largest)
#             self.max_heapify(largest)
    
#     def extract_max(self):
#         if not len(self.heap):
#             return None
        
#         root = self.heap[0]
        
#         self.heap[0] = self.heap[-1]
#         self.heap.pop()
        
#         if self.heap:
#             self.max_heapify(0)
        
#         return root

#     def print_heap(self):
#         print(self.heap)


# class BST:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
    
#     def add_child(self, data):
#         if self.data == data:
#             return None
        
#         if data < self.data:
#             if self.left:
#                 self.left.add_child(data)
#             else:
#                 self.left = BST(data)
#         else:
#             if self.right:
#                 self.right.add_child(data)
#             else:
#                 self.right = BST(data)
        
#     def in_order_traversal(self):
#         elements = []
#         if self.left:
#             elements += self.left.in_order_traversal()
#         elements.append(self.data)
#         if self.right:
#             elements += self.right.in_order_traversal()
        
#         return elements

# def build_tree(arr):
#     if len(arr) <= 0:
#         return None
    
#     root = BST(arr[0])
#     for i in range(1, len(arr)):
#         root.add_child(arr[i])
#     return root
    
# heap = MHeap()

# arr = [[23,56,12],[23,65,90]]

# for i in arr:
#     for j in i:
#         heap.insert(j)

# largest = []

# for i in range(3):
#     largest.append(heap.extract_max())

# bst = build_tree(largest)
# print(bst.in_order_traversal())



# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.end_of_word = False

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
        
#     def insert(self, word):
#         node = self.root
        
#         for char in word:
#             if char not in node.children:
#                 node.children[char] = TrieNode()
#             node = node.children[char]
        
#         node.end_of_word = True
    
#     def search(self, word):
#         node = self.root
        
#         for char in word:
#             if char not in node.children:
#                 return False
#             node = node.children[char]
#         return node.end_of_word
    
#     def starts_with(self, prefix):
#         node = self.root
        
#         for char in prefix:
#             if char not in node.children:
#                 return False
#             node = node.children[char]
#         return True
    
#     def delete(self, word):
#         def delete_recursive(node, word, depth):
#             if not node:
#                 return False
            
#             if depth == len(word):
#                 if node.end_of_word:
#                     node.end_of_word = False
#                 return len(node.children) == 0
            
#             char = word[depth]
            
#             if char in node.children:
#                 delete_current_node = delete_recursive(node.children[char], word, depth + 1)
                
#                 if delete_current_node:
#                     del node.children[char]
#                     return len(node.children) == 0 and not node.end_of_word
            
#             return False
#         delete_recursive(self.root, word, 0)


# tree = Trie()
# tree.insert("apple")
# tree.insert("add")
# tree.insert("app")
# tree.insert("all")
# tree.insert("allow")

# print(tree.search("applerr"))



# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



# class Graph:
#     def __init__(self, edges):
#         self.dict = {}
#         self.edges = edges
        
#         for start, end in self.edges:
#             if start in self.dict:
#                 self.dict[start].append(end)
#             else:
#                 self.dict[start] = [end]
#         print(self.dict)
    
#     def add_vertex(self, vertex):
#         if vertex not in self.dict:
#             self.dict[vertex] = []
#             print(vertex)
#         else:
#             print("Already Exist")
    
#     def add_edges(self, start, edge):
#         if start in self.dict:
#             self.dict[start].append(edge)
#         else:
#             self.dict[start] = [edge]
        
#         if start not in self.dict:
#             self.dict[edge] = []
        
#         print(self.dict)
#         print(f"Edge {start} -> {edge} added")
    
#     def get_paths(self, start, end, path=[]):
#         path = path + [start]
        
#         if start == end:
#             return [path]
        
#         if start not in self.dict:
#             return []
    
#         paths = []
#         for node in self.dict[start]:
#             if node not in path:
#                 new_paths = self.get_paths(node, end, path)
#                 for p in new_paths:
#                     paths.append(p)
#         return paths
    
#     def get_shortest_path(self, start, end, path=[]):
#         all_paths = self.get_paths(start, end)
        
#         if not all_paths:
#             return None
        
#         shortest_path = min(all_paths, key=len)
#         return shortest_path
    
#     def has_path(self, start, end):
#         return bool(self.get_paths(start, end))
    
#     def display(self):
#         if self.dict:
#             for key in self.dict:
#                 print(key, self.dict[key])


# if __name__ == "__main__":
#     routes = [
#         ("A", "B"),
#         ("A", "C"),
#         ("B", "D"),
#         ("C", "D"),
#         ("D", "E"),
#         ("E", "F"),
#         ("F", "G"),
#     ]

    
#     route_graph = Graph(routes)

#     route_graph.add_vertex('F')
    
#     route_graph.add_edges('G', 'D')  
#     route_graph.add_edges('H', 'D')  
#     route_graph.add_edges('E', 'A')  

    
#     route_graph.display()

    
#     start = "A"
#     end = "D"
#     print(f"All paths from {start} to {end}: {route_graph.get_paths(start, end)}")
#     print(f"Shortest path from {start} to {end}: {route_graph.get_shortest_path(start, end)}")



# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




# class BinarySearchTree:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
    
#     def add_child(self, data):
#         if data == self.data:
#             return 
        
#         if data < self.data:
#             if self.left:
#                 self.left.add_child(data)
#             else:
#                 self.left = BinarySearchTree(data)
#         if data > self.data:
#             if self.right:
#                 self.right.add_child(data)
#             else:
#                 self.right = BinarySearchTree(data)
                
#     def search(self, data):
#         if data == self.data:
#             return True
        
#         if data < self.data:
#             if self.left:
#                 return self.left.search(data)
#             else:
#                 return False
#         if data > self.data:
#             if self.right:
#                 return self.right.search(data)
#             else:
#                 return False
    
#     def find_max(self):
#         if self.right is None:
#             return self.data
#         return self.right.find_max()
    
#     def find_min(self):
#         if self.left is None:
#             return self.data
#         return self.left.find_min()
    
#     def find_left_count(self):
#         if self.left is None:
#             return 0
#         return 1 + self.left.find_left_count()
    
#     def find_right_count(self):
#         if self.right is None:
#             return 0
#         return 1 + self.right.find_right_count()
        
    
#     def find_second_largest(self):
#         if not self.right and self.left:
#             return None
        
#         parent = 0
#         current = self
        
#         while current.right:
#             parent = current.right
#             current = current.right
        
#         if current.left:
#             return current.left.find_max().data
        
#         if parent:
#             return parent.data
        
#         return None
    
#     def find_second_smallest(self):
#         if not self.left and self.right:
#             return None
        
#         parent = 0
#         current = self
        
#         while current.left:
#             parent = current.left
#             current = current.left
        
#         if current.right:
#             return current.right.find_min()

#         if parent:
#             return parent.data
        
#         return None
    
#     def in_order_traversal(self):
#         element = []
#         if self.left:
#             element += self.left.in_order_traversal()
#         element.append(self.data)
#         if self.right:
#             element += self.right.in_order_traversal()
#         return element
    
#     def pre_order_traversal(self):
#         element = [self.data]
#         if self.left:
#             element += self.left.pre_order_traversal()
        
#         if self.right:
#             element += self.right.pre_order_traversal()
#         return element
    
#     def post_order_traversal(self):
#         element = []
#         if self.left:
#             element += self.left.post_order_traversal()
#         if self.right:
#             element += self.right.post_order_traversal()
#         element.append(self.data)
#         return element
    
#     def delete(self, data):
#         if data < self.left:
#             if self.left:
#                 self.left = self.left.delete(data)
        
#         elif data > self.data:
#             if self.right:
#                 self.right = self.right.delete(data)
        
#         else:
#             if not self.right and not self.left:
#                 return None
            
#             if self.left is None:
#                 return self.right
            
#             if self.right is None:
#                 return self.left
            
#             min_val = self.right.find_min()
#             self.data = min_val
#             self.right = self.right.delete(min_val)
            
#         return self
    

# def build_tree(self, arr):
#     root = BinarySearchTree(arr[0])
#     for i in range(1, len(arr)):
#         root.add_child(arr[i])
#     return root





# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



# class GraphTree:
#     def __init__(self, edges):
#         self.edges = edges
#         self.children = {}
#         for start, end in edges:
#             if start in self.children:
#                 self.children[start].append(end)
#             else:
#                 self.children[start] = [end]
    
#     def vertex(self, vertex):
#         if vertex not in self.children:
#             self.children[vertex] = []
    
#     def add_edge(self, start, end):
#         if start in self.children:
#             self.children[start].append(end)
#         else:
#             self.children[start] = [end]
    
#     def get_paths(self, start, end, path=[]):
#         path = path + [start]
        
#         if start == end:
#             return [path]
        
#         if start not in self.children:
#             return []
        
#         paths = []
#         for node in self.children[start]:
#             if node not in path:
#                 new_path = self.get_paths(node, end, path)
#                 for p in new_path:
#                     paths.append(p)

#         return paths            
    
#     def get_shortest(self, start, end):
#         new_path = self.get_paths(start, end)
#         if not new_path:
#             return None
#         shortest_path = min(new_path, key=len)
        
#         return shortest_path
    
#     def has_path(self, start, end):
#         return bool(self.get_paths(start, end))
    
#     def display(self):
#         for i in self.children:
#             print(i, self.children[i])



# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# class MinHeap:
#     def __init__(self):
#         self.heap = []
    
#     def parent(self, i):
#         return (i - 1) // 2
    
#     def left(self, i):
#         return (i * 2) +1
    
#     def right(self, i):
#         return (i * 2) + 2
    
#     def insert(self, data):
#         self.heap.append(data)

#         current = len(self.heap)-1
#         while current > 0 and self.heap[current] < self.heap[self.parent(current)]:
#             self.heap[current], self.heap[self.parent(current)]  = self.heap[self.parent(current)], self.heap[current] 
#             current = self.parent(current)
    
#     def heapify(self, data):
#         left = self.left(data)
#         right = self.right(data)
        
#         smallest = data
        
#         if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
#             smallest = left
        
#         if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
#             smallest = right
            
#         if smallest != data:
#             self.heap[data], self.heap[smallest]  = self.heap[smallest], self.heap[data]
#             self.heapify(smallest)
    
#     def extract_min(self):
#         if len(self.heap) == 0:
#             return None
#         root = self.heap[0]
        
#         self.heap[0] = self.heap[-1]
#         self.heap.pop()
#         self.heapify(0)
        
#         return root

#     def increase_key(self, i,  new_val):
#         self.heap[i] = new_val
        
#         while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
#             self.heap[i], self.heap[self.parent(i)]  = self.heap[self.parent(i)], self.heap[i] 
#             i = self.parent(i)
    
#     def delete_key(self, key):
#         if 0 <= key < len(self.heap):
#             self.increase_key(key, float('-inf'))
#             self.extract_min()

#     def heap_sort(self):
#         sorted_array = []
#         while len(self.heap) > 0:
#             sorted_array.append(self.extract_min())
#         return sorted_array


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////





# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////