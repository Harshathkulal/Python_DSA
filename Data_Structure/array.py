class Array:
    def __init__(self):
        self.length = 0
        self.data = []

    def get(self, index):
        if 0 <= index < self.length:
            return self.data[index]
        return None

    def push(self, item):
        self.data.append(item)
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    def delete(self, index):
        if 0 <= index < self.length:
            deleted_item = self.data[index]
            del self.data[index]
            self.length -= 1
            return deleted_item
        return None

    def __str__(self):
        return str(self.data)


# Example usage:
arr = Array()
arr.push(5)
arr.push(10)
arr.push(15)
arr.push(20)
print(arr)  # Output: [5, 10, 15, 20]

arr.pop()
print(arr)  # Output: [5, 10, 15]

arr.delete(1)
print(arr)  # Output: [5, 15]

print(arr.get(1))  # Output: 15

