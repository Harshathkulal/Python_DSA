class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hash_value = self._hash(key)
        for pair in self.table[hash_value]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[hash_value].append((key, value))

    def get(self, key):
        hash_value = self._hash(key)
        for pair in self.table[hash_value]:
            if pair[0] == key:
                return pair[1]
        raise KeyError(f"Key '{key}' not found")

    def delete(self, key):
        hash_value = self._hash(key)
        for i, pair in enumerate(self.table[hash_value]):
            if pair[0] == key:
                del self.table[hash_value][i]
                return
        raise KeyError(f"Key '{key}' not found")

# Example usage:
hash_table = HashTable(size=10)
hash_table.insert("apple", 5)
hash_table.insert("banana", 7)
hash_table.insert("orange", 10)

print(hash_table.get("apple"))  # Output: 5
print(hash_table.get("banana"))  # Output: 7

hash_table.insert("banana", 8)  # Update value for existing key
print(hash_table.get("banana"))  # Output: 8

hash_table.delete("orange")
# print(hash_table.get("orange"))  # Raises KeyError since "orange" is deleted
