def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if found
    return -1  # Return -1 if not found

# Example usage:
my_list = [2, 4, 7, 10, 13, 18, 22, 27, 31]

# Finding the index of 13 in the list
index = linear_search(my_list, 13)
if index != -1:
    print("Element found at index:", index)
else:
    print("Element not found in the list")
