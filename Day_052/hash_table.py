class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # Create a list of empty lists for chaining

    # Hash function to map a key to an index
    def hash_function(self, key):
        return hash(key) % self.size
    
    # Insert (put) a key-value pair into the hash table
    def put(self, key, value):
        index = self.hash_function(key)
        # Check if the key already exists and update it if found
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # If key doesn't exist, append the new key-value pair
        self.table[index].append([key, value])
    
    # Retrieve (get) the value associated with a key
    def get(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]  # Return the value if the key is found
        return None  # Return None if the key is not found
    
    # Remove a key-value pair from the hash table
    def remove(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                return
        raise KeyError("Key not found.")
    
    # Display the hash table
    def display(self):
        for index, bucket in enumerate(self.table):
            print(f"Index {index}: {bucket}")

# Example usage:
hash_table = HashTable()

# Insert some key-value pairs
hash_table.put("apple", 1)
hash_table.put("banana", 2)
hash_table.put("grape", 3)
hash_table.put("orange", 4)

# Display the hash table
hash_table.display()
# Output:
# Index 0: []
# Index 1: []
# Index 2: [['orange', 4]]
# Index 3: [['grape', 3]]
# Index 4: []
# Index 5: []
# Index 6: []
# Index 7: [['apple', 1]]
# Index 8: []
# Index 9: [['banana', 2]]

# Get the value for a key
print("Value for key 'apple':", hash_table.get("apple"))  # Output: 1

# Remove a key
hash_table.remove("banana")
hash_table.display()
# Output (after removing banana):
# Index 9: []

# Try to get a key that doesn't exist
print("Value for key 'banana':", hash_table.get("banana"))  # Output: None
