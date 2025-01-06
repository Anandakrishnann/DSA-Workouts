class HashMap:
    def __init__(self, size):
        """
        Initialize the hash map with a fixed size and empty slots (None).
        """
        self.size = size
        self.table = [None] * self.size  # Create an empty hash table

    def hash_function(self, key):
        """
        Generate an index for the given key using a hash function.
        The index is the remainder of the key's hash value divided by the table size.
        """
        index = hash(key) % self.size
        return index

    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table using open addressing to handle collisions.
        """
        index = self.hash_function(key)  # Get the hashed index
        start_index = index  # Save the starting index to detect a full table

        # Loop to handle collisions using linear probing
        while self.table[index] is not None:
            if self.table[index][0] == key:  # Update value if key already exists
                self.table[index] = (key, value)
                return

            # Move to the next index (linear probing)
            index = (index + 1) % self.size

            # If we've looped back to the start, the table is full
            if index == start_index:
                print("Hash table is full!")
                return

        # Insert the key-value pair at the found empty slot
        self.table[index] = (key, value)

    def retrieve(self, key):
        """
        Retrieve the value associated with the given key.
        """
        index = self.hash_function(key)  # Get the hashed index
        start_index = index  # Save the starting index to detect a full search

        # Loop to search for the key using linear probing
        while self.table[index] is not None:
            if self.table[index][0] == key:  # Key found
                return self.table[index][1]

            # Move to the next index
            index = (index + 1) % self.size

            # If we've looped back to the start, the key does not exist
            if index == start_index:
                break

        return None  # Key not found

    def delete(self, key):
        """
        Delete a key-value pair from the hash table.
        """
        index = self.hash_function(key)  # Get the hashed index
        start_index = index  # Save the starting index to detect a full search

        # Loop to search for the key using linear probing
        while self.table[index] is not None:
            if self.table[index][0] == key:  # Key found
                self.table[index] = None  # Mark the slot as empty
                return

            # Move to the next index
            index = (index + 1) % self.size

            # If we've looped back to the start, the key does not exist
            if start_index == index:
                break

        return None  # Key not found

    def display(self):
        """
        Display the current state of the hash table.
        """
        for k, v in enumerate(self.table):
            print(k, v)


# Example usage of the HashMap
hash_map = HashMap(10)

# Insert key-value pairs into the hash table
hash_map.insert(3, "Orange")    # Hash to index 3
hash_map.insert(8, "Grapes")    # Collision at index 3, resolve using linear probing
hash_map.insert(13, "Banana")   # Another collision at index 3, resolved further

# Display the hash table after insertions
hash_map.display()
