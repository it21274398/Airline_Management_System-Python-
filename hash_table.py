class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            index = (index + 1) % self.size
            if index == original_index:
                raise Exception("Hash table is full")
        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == original_index:
                break
        return None

    def delete(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return
            index = (index + 1) % self.size
            if index == original_index:
                break


# Example usage for testing purposes
if __name__ == "__main__":
    hash_table = HashTable(10)
    hash_table.insert('JFK', 'John F. Kennedy International Airport')
    hash_table.insert('LAX', 'Los Angeles International Airport')
    print(hash_table.search('JFK'))  # Output: John F. Kennedy International Airport
    print(hash_table.search('LAX'))  # Output: Los Angeles International Airport
    hash_table.delete('JFK')
    print(hash_table.search('JFK'))  # Output: None
