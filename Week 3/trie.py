class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word): 
        node = self.root

        for char in word:
            
            if char not in node.children:
                node.children[char] = TrieNode()  
            node = node.children[char]
            
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word 

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def delete(self, word):
        def delete_recursive(node, word, depth):
            if not node:
                return False

            if depth == len(word):
                if node.is_end_of_word:
                    node.is_end_of_word = False
                return len(node.children) == 0

            char = word[depth]
            if char in node.children:
                should_delete_current_node = delete_recursive(node.children[char], word, depth + 1)

                if should_delete_current_node:
                    del node.children[char]
                    return len(node.children) == 0 and not node.is_end_of_word

            return False

        delete_recursive(self.root, word, 0)


# Example usage
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("bat")
trie.insert("ball")
trie.insert("allow")
trie.insert("act")
trie.insert("add")


print(trie.search("apple"))  # Trueff
print(trie.search("ap"))    # True
print(trie.search("bat"))    # True
print(trie.search("ball"))   # True
print(trie.search("cat"))    # False
print(trie.starts_with("ap"))  # True
print(trie.starts_with("ba"))  # True
print(trie.starts_with("ca"))  # False

trie.delete("app")
print(trie.search("app"))  # False
print(trie.search("apple"))  # True
h = trie.root.children['b'].children['a'].children.keys()
print(h)
print("__" * 74)
