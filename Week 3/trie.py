class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.is_end_of_word = False  # Flag to indicate if the node is the end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()  # The root of the trie is an empty TrieNode

    # Method to insert a word into the trie
    def insert(self, word): 
        node = self.root  # Start from the root node

        for char in word:
            # If the character is not already a child of the current node, add it
            if char not in node.children:
                node.children[char] = TrieNode()  
            node = node.children[char]  # Move to the next node in the trie

        node.is_end_of_word = True  # Mark the end of the word

    # Method to search for a word in the trie
    def search(self, word):
        node = self.root  # Start from the root node

        for char in word:
            # If a character is not found, return False
            if char not in node.children:
                return False
            node = node.children[char]  # Move to the next node

        return node.is_end_of_word  # Return True if it's the end of the word

    # Method to check if there is any word in the trie that starts with the given prefix
    def starts_with(self, prefix):
        node = self.root  # Start from the root node

        for char in prefix:
            # If a character is not found, return False
            if char not in node.children:
                return False
            node = node.children[char]  # Move to the next node

        return True  # If the loop completes, the prefix exists in the trie

    # Method to delete a word from the trie
    def delete(self, word):
        # Helper function to recursively delete a word
        def delete_recursive(node, word, depth):
            if not node:
                return False  # If node is None, return False

            if depth == len(word):
                # If we've reached the end of the word
                if node.is_end_of_word:
                    node.is_end_of_word = False  # Unmark the end of the word
                return len(node.children) == 0  # If there are no children, the node can be deleted

            char = word[depth]
            if char in node.children:
                should_delete_current_node = delete_recursive(node.children[char], word, depth + 1)

                # If the child node should be deleted, remove it
                if should_delete_current_node:
                    del node.children[char]
                    return len(node.children) == 0 and not node.is_end_of_word  # Delete current node if it has no children and is not the end of a word

            return False  # If the word doesn't exist, return False

        delete_recursive(self.root, word, 0)  # Start the recursive deletion from the root

# Example usage
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("bat")
trie.insert("ball")
trie.insert("allow")
trie.insert("act")
trie.insert("add")

# Test search
print(trie.search("apple"))  # True
print(trie.search("ap"))    # True
print(trie.search("bat"))    # True
print(trie.search("ball"))   # True
print(trie.search("cat"))    # False

# Test starts_with
print(trie.starts_with("ap"))  # True
print(trie.starts_with("ba"))  # True
print(trie.starts_with("ca"))  # False

# Test delete
trie.delete("app")
print(trie.search("app"))  # False
print(trie.search("apple"))  # True

# Check the children of the 'b' node
h = trie.root.children['b'].children['a'].children.keys()
print(h)  # Should print the children of the node with the character 'a'

print("__" * 74)  # Just for formatting the output
