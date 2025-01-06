class Node:
    def __init__(self, data):
        """
        Initialize a node with the given data.
        The node has 'next' and 'prev' pointers, initially set to None.
        """
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        """
        Initialize an empty doubly linked list with head and tail pointers set to None.
        """
        self.head = None
        self.tail = None

    def add_node(self, data):
        """
        Add a new node with the given data to the end of the list.
        """
        new_node = Node(data)

        if self.head is None:
            # If the list is empty, set the new node as both head and tail
            self.head = new_node
        else:
            # Link the new node to the current tail and update the tail pointer
            self.tail.next = new_node
            new_node.prev = self.tail

        self.tail = new_node

    def add_node_after(self, target, data):
        """
        Add a new node with the given data after the node containing the target value.
        """
        node = Node(data)
        temp = self.head

        # Traverse the list to find the target node
        while temp is not None and temp.data != target:
            temp = temp.next

        if temp is None:
            # If the target node is not found, exit the function
            return

        if temp == self.tail:
            # If the target node is the tail, append the new node at the end
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            # Insert the new node after the target node
            node.next = temp.next
            temp.next.prev = node
            temp.next = node
            node.prev = temp

    def recursion(self, data):
        """
        Reverse the doubly linked list recursively.
        """
        if data is None:
            return

        # Swap the 'next' and 'prev' pointers of the current node
        data.next, data.prev = data.prev, data.next

        if data.prev is None:
            # If we reach the new head, update the head pointer
            self.head = data
            return

        # Recur for the previous node (which is the original next node)
        self.recursion(data.prev)

    def node_delete(self, data):
        """
        Delete the first node with the specified data.
        """
        temp = self.head

        # Case 1: The list has only one node
        if temp == self.tail and temp == self.head:
            self.head = None
            self.tail = None
            return

        # Case 2: The node to delete is the head
        if temp.data == data:
            self.head = temp.next
            self.head.prev = None
            return

        # Traverse the list to find the node to delete
        while temp is not None and temp.data != data:
            temp = temp.next

        if temp is None:
            # If the node is not found, exit the function
            return

        # Case 3: The node to delete is the tail
        if temp == self.tail:
            self.tail = temp.prev
            self.tail.next = None
        else:
            # Case 4: The node to delete is in the middle
            temp.prev.next = temp.next
            temp.next.prev = temp.prev

    def print_list(self):
        """
        Print the list from head to tail.
        """
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def print_list_reverse(self):
        """
        Print the list from tail to head.
        """
        temp = self.tail
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.prev
        print("None")

# Create a new doubly linked list
list1 = DoublyLinkedList()

# Add nodes to the list
list1.add_node(1)
list1.add_node(2)
list1.add_node(3)
list1.add_node(5)

# Add a node with value 4 after the node with value 3
list1.add_node_after(3, 4)

# Delete the node with value 5
list1.node_delete(5)

# Reverse the doubly linked list recursively
list1.recursion(list1.head)

# Print the list from head to tail
list1.print_list()

# Print the list from tail to head
list1.print_list_reverse()
