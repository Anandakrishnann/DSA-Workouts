class HashMap:
    def __init__(self, size):
        """
        Initialize the HashMap with a given size.
        
        Args:
        - size (int): Size of the hash table (number of buckets).
        """
        self.size = size
        self.table = [[] for _ in range(self.size)]  # Create a list of empty buckets

    def hash_function(self, key):
        """
        Compute the hash index for a given key.
        
        Args:
        - key: The key to hash.
        
        Returns:
        - int: The index in the hash table.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Insert or update a key-value pair in the hash map.
        
        Args:
        - key: The key to insert.
        - value: The value associated with the key.
        """
        index = self.hash_function(key)
        bucket = self.table[index]

        # Check if the key already exists and update its value
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # If the key does not exist, append it to the bucket
        bucket.append((key, value))

    def retrieve(self, key):
        """
        Retrieve the value associated with a key.
        
        Args:
        - key: The key to search for.
        
        Returns:
        - The value associated with the key, or None if the key is not found.
        """
        index = self.hash_function(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None  # Key not found

    def delete(self, key):
        """
        Delete a key-value pair from the hash map.
        
        Args:
        - key: The key to delete.
        
        Returns:
        - bool: True if the key was deleted, False if the key was not found.
        """
        index = self.hash_function(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False  # Key not found

    def display(self):
        """
        Display the contents of the hash map.
        """
        for i, bucket in enumerate(self.table):
            if bucket:  # Only display non-empty buckets
                print(f"Bucket {i}: {bucket}")


# Example usage
hash_map = HashMap(size=5)

# Insert key-value pairs
hash_map.insert(3, "Orange")    # 3 % 5 == 3
hash_map.insert(8, "Grapes")    # 8 % 5 == 3 (collision with 3)
hash_map.insert(1, "Apple")     # 1 % 5 == 1
hash_map.insert(6, "Banana")    # 6 % 5 == 1 (collision with 1)

# Update the value of an existing key
hash_map.insert(3, "Mango")  # Update key 3's value

# Retrieve a value
print("Retrieve key 3:", hash_map.retrieve(3))  # Output: Mango

# Delete a key
hash_map.delete(8)  # Remove key 8 (Grapes)

# Display the hash table after the operations
print("HashMap Contents:")
hash_map.display()
