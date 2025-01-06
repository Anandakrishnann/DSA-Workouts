class Node:
    def __init__(self, data):
        # Initialize a node with data, and set next pointer to None
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        # Initialize an empty linked list with head and tail pointers set to None
        self.head = None
        self.tail = None

    def add_node(self, data):
        # Add a new node with the given data to the end of the list
        new_node = Node(data)

        if self.head is None:
            # If the list is empty, set the new node as both head and tail
            self.head = new_node
            self.tail = new_node
        else:
            # Otherwise, link the new node to the end of the list
            self.tail.next = new_node
            self.tail = new_node

    def node_delete(self, data):
        # Delete the first node with the specified data
        node = self.head
        prev_node = None

        if node is not None and node.data == data:
            # Case 1: The node to delete is the head
            self.head = node.next
            return

        # Traverse the list to find the node to delete
        while node is not None and node.data != data:
            prev_node = node
            node = node.next

        if node is None:
            # If the node is not found, exit the function
            return

        if node == self.tail:
            # Case 2: The node to delete is the tail
            self.tail = prev_node
            prev_node.next = None
            return

        # Case 3: The node to delete is in the middle
        prev_node.next = node.next

    def middle_element_delete(self):
        # Delete the middle element of the linked list
        slow_ptr = self.head
        fast_ptr = self.head
        prev = None

        # Use two pointers to find the middle node
        while fast_ptr is not None and fast_ptr.next is not None:
            prev = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        if prev is not None:
            # Remove the middle node
            prev.next = slow_ptr.next

            # Update the tail if the middle node was the last node
            if slow_ptr == self.tail:
                self.tail = prev

    def add_node_after(self, target, data):
        # Add a new node with the given data after the node containing the target value
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
            self.tail = node
        else:
            # Insert the new node after the target node
            node.next = temp.next
            temp.next = node

    def print_list(self):
        # Print the list from head to tail
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Create a new linked list
linked_list = LinkedList()

# Add nodes to the list
linked_list.add_node(1)
linked_list.add_node(2)
linked_list.add_node(3)
linked_list.add_node(4)

# Delete the node with value 1
linked_list.node_delete(1)

# Add a node with value 5 after the node with value 2
linked_list.add_node_after(2, 5)

# Print the current list
linked_list.print_list()
