class BinarySearchTreeNode:
    def __init__(self, data):
        # Initialize the node with data and set left and right children as None
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        # Add a child node to the tree while maintaining BST properties
        if data == self.data:  # Ignore duplicate values
            return
        
        if data < self.data:
            # If data is smaller, go to the left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # If data is larger, go to the right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def find_maximum(self):
        # Find the maximum value by traversing to the far-right node
        if self.right is None:
            return self.data
        return self.right.find_maximum()

    def find_minimum(self):
        # Find the minimum value by traversing to the far-left node
        if self.left is None:
            return self.data
        return self.left.find_minimum()

    def find_left_count(self):
        # Count nodes in the left subtree
        if self.left is None:
            return 0
        return 1 + self.left.find_left_count()

    def find_right_count(self):
        # Count nodes in the right subtree
        if self.right is None:
            return 0
        return 1 + self.right.find_right_count()

    def in_order_traversal(self):
        # Traverse in order: Left → Root → Right
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def pre_order_traversal(self):
        # Traverse in pre-order: Root → Left → Right
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

    def post_order_traversal(self):
        # Traverse in post-order: Left → Right → Root
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements

    def search(self, val):
        # Search for a value in the BST
        if val == self.data:
            return True
        if val < self.data:
            # If value is smaller, search in the left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            # If value is larger, search in the right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_second_largest(self):
        # Find the second-largest value in the BST
        if not self.left and not self.right:
            return None  # Only one node exists, no second-largest

        parent = None
        current = self
        
        # Traverse to the rightmost node
        while current.right:
            parent = current
            current = current.right
        
        # If the largest node has a left subtree, find the max there
        if current.left:
            return current.left.find_maximum()
        
        # If no left subtree, return the parent node
        if parent:
            return parent.data

        return None

    def find_second_minimum(self):
        # Find the second-smallest value in the BST
        if not self.left and not self.right:
            return None  # Only one node exists, no second-smallest

        parent = None
        current = self
        
        # Traverse to the leftmost node
        while current.left:
            parent = current
            current = current.left
        
        # If the smallest node has a right subtree, find the min there
        if current.right:
            return current.right.find_minimum()
        
        # If no right subtree, return the parent node
        if parent:
            return parent.data
        
        return None

    def delete(self, val):
        # Delete a node with the given value
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)  # Recursively delete in the left subtree
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)  # Recursively delete in the right subtree
        else:
            # Node to be deleted found
            if self.left is None and self.right is None:
                return None  # Node is a leaf
            if self.left is None:
                return self.right  # Node has only a right child
            if self.right is None:
                return self.left  # Node has only a left child
            # Node has two children: Replace with the smallest value in the right subtree
            min_val = self.right.find_minimum()
            self.data = min_val
            self.right = self.right.delete(min_val)  # Delete the duplicate in the right subtree
        return self


# Function to check if the tree is a valid BST
def is_bst(node, min_value=float('-inf'), max_value=float('inf')):
    if node is None:
        return True
    if not (min_value < node.data < max_value):
        return False
    return (is_bst(node.left, min_value, node.data) and
            is_bst(node.right, node.data, max_value))


# Function to build a BST from a list of numbers
def build_tree(numbers):
    root = BinarySearchTreeNode(numbers[0])  # First number becomes the root
    for i in range(1, len(numbers)):
        root.add_child(numbers[i])
    return root


# Example usage of the BinarySearchTreeNode class
if __name__ == '__main__':
    numbers = [23, 4, 23, 66, 63, 12, 674, 12, 2]
    number_tree = build_tree(numbers)
    
    print("In-order Traversal:", number_tree.in_order_traversal())
    print("Pre-order Traversal:", number_tree.pre_order_traversal())
    print("Post-order Traversal:", number_tree.post_order_traversal())
    print("Minimum value in the tree:", number_tree.find_minimum())
    print("Maximum value in the tree:", number_tree.find_maximum())
    
    number_tree.delete(66)
    print("In-order after deleting 66:", number_tree.in_order_traversal())
    
    print("Searching for value 9:", number_tree.search(9))
    print("Searching for value 63:", number_tree.search(63))
    
    print("Is it a valid BST?", is_bst(number_tree))
    print("Second-largest value:", number_tree.find_second_largest())
    print("Second-smallest value:", number_tree.find_second_minimum())
