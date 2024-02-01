class MyString:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

    def length(self):
        return len(self.value)

    def concatenate(self, other):
        if isinstance(other, MyString):
            return MyString(self.value + other.value)
        else:
            raise TypeError("Can only concatenate with another MyString")

    def get_character(self, index):
        if 0 <= index < len(self.value):
            return self.value[index]
        else:
            raise IndexError("Index out of range")

# Example usage:
my_string1 = MyString("Hello")
my_string2 = MyString(" World!")

print(my_string1.length())            # Output: 5
print(my_string1.concatenate(my_string2))  # Output: Hello World!
print(my_string1.get_character(2))    # Output: l

