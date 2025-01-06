class QueueUsingStack:
    def __init__(self):
        """
        Initialize the queue using two stacks:
        - s1: Stack to handle enqueue operations
        - s2: Stack to handle dequeue and peek operations
        """
        self.s1 = []  # Main stack for enqueue
        self.s2 = []  # Auxiliary stack for dequeue and peek

    def enqueue(self, data):
        """
        Add an element to the queue.
        Since we are using stacks, the element is pushed onto s1.
        """
        self.s1.append(data)

    def dequeue(self):
        """
        Remove and return the front element of the queue.
        - If both s1 and s2 are empty, the queue is empty, so return None.
        - If s2 is empty, transfer all elements from s1 to s2 (reversing their order).
        - Pop and return the top element from s2, which represents the front of the queue.
        """
        if not self.s1 and not self.s2:  # Both stacks are empty
            return None

        if not self.s2:  # Transfer elements from s1 to s2 if s2 is empty
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2.pop()  # Pop the front element from s2

    def peek(self):
        """
        Return the front element of the queue without removing it.
        - If both s1 and s2 are empty, the queue is empty, so return None.
        - If s2 is empty, transfer all elements from s1 to s2.
        - Return the top element from s2, which represents the front of the queue.
        """
        if not self.s1 and not self.s2:  # Both stacks are empty
            return None

        if not self.s2:  # Transfer elements from s1 to s2 if s2 is empty
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2[-1]  # Return the front element (top of s2)

    def is_empty(self):
        """
        Check if the queue is empty.
        - The queue is empty if both s1 and s2 are empty.
        """
        return len(self.s1) == 0 and len(self.s2) == 0

    def display(self):
        """
        Display the elements of the queue in order.
        - s2[::-1] contains the front elements in the correct order.
        - s1 contains the back elements in reverse order.
        - Combine the two lists to show the queue from front to back.
        """
        if not self.s1 and not self.s2:  # Queue is empty
            return None
        else:
            q_display = self.s2[::-1] + self.s1  # Combine reversed s2 and s1
            print(q_display)  # Print the queue representation


# Example usage of QueueUsingStack
stack = QueueUsingStack()
stack.enqueue(1)  # Add element 1 to the queue
stack.enqueue(2)  # Add element 2 to the queue
stack.enqueue(3)  # Add element 3 to the queue
stack.enqueue(4)  # Add element 4 to the queue
stack.enqueue(5)  # Add element 5 to the queue

print(stack.dequeue())  # Remove and print the front element (1)
print(stack.peek())     # Print the front element without removing it (2)
print(stack.is_empty()) # Check if the queue is empty (False)
print(stack.display())  # Display the current queue ([2, 3, 4, 5])
