# Class to represent each node in the tree (e.g., employees in a company)
class TreeNode:
    def __init__(self, data):
        self.data = data  # The name or title of the node (e.g., CEO, CTO, etc.)
        self.children = []  # List of child nodes (e.g., subordinates of the current node)
        self.parent = None  # Parent node (e.g., the boss or supervisor of the current node)

    # Method to add a child node to the current node
    def add_child(self, data):
        data.parent = self  # Set the parent of the child node as the current node
        self.children.append(data)  # Add the child node to the children list of the current node

    # Method to get the level of the current node (i.e., its depth in the tree)
    def get_level(self):
        level = 0  # Start at level 0 for the root node
        p = self.parent  # Start from the parent of the current node
        while p:
            level += 1  # Move upwards in the tree, increasing the level each time
            p = p.parent  # Move to the parent's parent
        return level  # Return the level (depth) of the current node

    # Method to print the tree structure in a readable format
    def print_tree(self):
        space = " " * self.get_level() * 3  # Indentation based on the level of the node
        prefix = space + "|__" if self.parent else ""  # Add prefix to show hierarchy
        print(prefix + self.data)  # Print the data of the current node
        for child in self.children:  # Recursively print the children nodes
            child.print_tree()  # Print each child's tree (subordinate's hierarchy)

# Creating the root of the company tree
company = TreeNode("Fadex9")

# Creating a tree for the CEO and adding children (subordinates)
tree = TreeNode("CEO")
tree.add_child(TreeNode("Anandha Krishnan"))  # Adding a child to the CEO (e.g., an employee)

# Creating a tree for the CTO and adding children (subordinates)
cto = TreeNode("CTO")
cto.add_child(TreeNode("Amal"))  # Adding a child under the CTO (e.g., a team member)

# Creating a tree for a SWEEPER role and adding a child
sweeper = TreeNode('SWEEPER')
sweeper.add_child(TreeNode("Saniya"))  # Adding a child under SWEEPER

# Adding CEO, CTO, and SWEEPER under the company node (the root of the tree)
company.add_child(tree)  # Adding CEO to the company hierarchy
company.add_child(cto)  # Adding CTO to the company hierarchy
company.add_child(sweeper)  # Adding SWEEPER to the company hierarchy

# Printing the entire tree structure starting from the company node
company.print_tree()
