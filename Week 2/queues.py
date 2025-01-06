class Queue:
    def __init__(self):
        """
        Initialize the queue using a list.
        """
        self.queue = []  # List to store queue elements

    def enqueue(self, data):
        """
        Add an element to the end of the queue.
        """
        self.queue.append(data)

    def dequeue(self):
        """
        Remove and return the front element of the queue.
        """
        dequeued_item = self.queue.pop(0)  # Remove the first element
        return dequeued_item

    def is_empty(self):
        """
        Check if the queue is empty.
        Returns True if the queue has no elements, otherwise False.
        """
        return len(self.queue) == 0

    def display(self):
        """
        Display all elements in the queue.
        """
        print(self.queue)

    def pops(self):
        """
        Remove and return the last element of the queue.
        """
        item = self.queue.pop()  # Remove the last element
        return item


def recu(queue):
    """
    Recursively pop and print all elements of the queue from the end.
    Stops when the queue is empty.
    """
    if queue.is_empty():  # Base case: If the queue is empty, stop recursion
        return
    print(queue.pops())  # Print the last element (popped)
    return recu(queue)   # Recursive call with the modified queue


# Example usage of the Queue class and the recursive function
queue = Queue()

queue.enqueue("Data 1")  # Add "Data 1" to the queue
queue.enqueue("Data 2")  # Add "Data 2" to the queue
queue.enqueue("Data 3")  # Add "Data 3" to the queue
queue.enqueue("Data 4")  # Add "Data 4" to the queue

a = recu(queue)  # Recursively print and remove elements from the end
