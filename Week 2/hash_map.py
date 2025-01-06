class HashTable:
    def __init__(self, size=10):
        """
        Initialize the hash table with a given size.
        Each index of the table is a list (bucket) to handle collisions using chaining.
        """
        self.size = size
        self.table = [[] for i in range(self.size)]

    def hash_function(self, key):
        """
        Calculate the hash value for a given key and map it within the table size.
        This ensures the key's index is within the range of the table.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.
        If the key already exists, update its value. Otherwise, add a new pair to the bucket.
        """
        index = self.hash_function(key)  # Get the index for the key
        bucket = self.table[index]  # Access the bucket at the index

        # Check if the key already exists in the bucket
        for i, kv in enumerate(bucket):
            k, v = kv
            if k == key:
                # Key exists; update the value
                bucket[i] = (key, value)
                return
        
        # Key does not exist; add a new key-value pair
        bucket.append((key, value))

    def retrieve(self, key):
        """
        Retrieve the value associated with a given key.
        Return None if the key does not exist.
        """
        index = self.hash_function(key)  # Get the index for the key
        bucket = self.table[index]  # Access the bucket at the index

        # Search for the key in the bucket
        for k, v in bucket:
            if k == key:
                return v  # Return the value if key is found
        return None  # Return None if key is not found

    def delete(self, key):
        """
        Delete a key-value pair from the hash table.
        Return True if the key is successfully deleted, False otherwise.
        """
        index = self.hash_function(key)  # Get the index for the key
        bucket = self.table[index]  # Access the bucket at the index

        # Search for the key in the bucket
        for i, kv in enumerate(bucket):
            k, v = kv
            if k == key:
                del bucket[i]  # Remove the key-value pair from the bucket
                return True  # Return True indicating successful deletion
        return False  # Return False if key is not found

    def display(self):
        """
        Display the hash table's contents, showing each bucket and its key-value pairs.
        """
        for i, bucket in enumerate(self.table):
            print(f"{i}: {bucket}")


# Example usage of the HashTable class
ht = HashTable()

# Insert key-value pairs
ht.insert("apple", 10)  # Add "apple" with value 10
ht.insert("banana", 20)  # Add "banana" with value 20
ht.insert("grape", 30)  # Add "grape" with value 30
ht.insert("orange", 40)  # Add "orange" with value 40

# Display the hash table
ht.display()

# Retrieve values for specific keys
print("Retrieve 'apple':", ht.retrieve("apple"))  # Output: 10
print("Retrieve 'banana':", ht.retrieve("banana"))  # Output: 20

# Delete a key-value pair
ht.delete("grape")  # Remove "grape" from the hash table

# Display the hash table after deletion
ht.display()

# Try retrieving a deleted key
print("Retrieve 'grape':", ht.retrieve("grape"))  # Output: None
