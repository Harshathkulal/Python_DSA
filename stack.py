class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")
            return None

    def size(self):
        return len(self.items)

# Example usage:
stack = Stack()

print("Is the stack empty?", stack.is_empty())  # Should print True

stack.push(5)
stack.push(10)
stack.push(15)

print("Size of the stack:", stack.size())  # Should print 3
print("Top element of the stack:", stack.peek())  # Should print 15

popped_item = stack.pop()
print("Popped item:", popped_item)  # Should print 15

print("Size of the stack after popping:", stack.size())  # Should print 2
print("Is the stack empty now?", stack.is_empty())  # Should print False
