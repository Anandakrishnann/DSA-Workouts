class StackUsingQueue:
    """
    Implement a stack using two queues.
    """
    def __init__(self):
        # Two queues are used to implement the stack
        self.q1 = []  # Main queue for stack operations
        self.q2 = []  # Temporary queue for rearranging elements
        
    def push(self, data):
        """
        Push an element onto the stack.
        """
        # Add the new element to q2 (acting as the top of the stack)
        self.q2.append(data)
        
        # Move all elements from q1 to q2 to maintain stack order
        while len(self.q1) > 0:
            self.q2.append(self.q1.pop(0))
        
        # Swap q1 and q2 to make q1 the main stack storage
        self.q2, self.q1 = self.q1, self.q2
        
    def pop(self):
        """
        Remove and return the top element of the stack.
        Returns None if the stack is empty.
        """
        if not self.is_empty():
            return self.q1.pop(0)  # Remove the front element of q1
        else:
            return None
        
    def peek(self):
        """
        Return the top element of the stack without removing it.
        Returns None if the stack is empty.
        """
        if not self.is_empty():
            return self.q1[0]  # Return the front element of q1
        else:
            return None
        
    def is_empty(self):
        """
        Check if the stack is empty.
        """
        return len(self.q1) == 0
    
    def display(self):
        """
        Display the current elements in the stack.
        """
        print(self.q1)


# Example usage of StackUsingQueue
stack = StackUsingQueue()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print(stack.pop())      # Output: 5 (top of the stack)
print(stack.is_empty()) # Output: False (stack is not empty)
print(stack.peek())     # Output: 4 (next top element)
stack.display()         # Output: [4, 3, 2, 1] (remaining stack elements)
