class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.data:
            return 
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
                print(f"{data} added")
            else:
                self.left = BinarySearchTree(data)
                
        if data > self.data:
            if self.right:
                self.right.add_child(data)
                print(f"{data} added")
            else:
                self.right = BinarySearchTree(data)
                

def is_bst(node, min_val=float('-inf'), max_val=float('inf')):
    if not node:
        return True
    
    if not(min_val < node.data < max_val):
        return False
    
    return (is_bst(node.left, min_val, node.data) and is_bst(node.right, node.data, max_val))

def build_tree(data):
    root = BinarySearchTree(data[0])
    for i in range(1, len(data)):
        root.add_child(data[i])

data = [10,2,4,6,37,23]

tree = build_tree(data)