def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_element = arr[mid]

        if mid_element == target:
            return mid
        elif mid_element < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found


# Example usage:
my_list = [2, 4, 7, 10, 13, 18, 22, 27, 31]

# Finding the index of 13 in the list
index = binary_search(my_list, 27)
if index != -1:
    print("Element found at index:", index)
else:
    print("Element not found in the list")
