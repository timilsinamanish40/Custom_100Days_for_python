def binary_search_recursive(arr, target, low, high):
    if low <= high:
        mid = (low + high) // 2
        # Check if the target is at the mid index
        if arr[mid] == target:
            return mid
        # If target is smaller, search in the left half
        elif arr[mid] > target:
            return binary_search_recursive(arr, target, low, mid - 1)
        # If target is larger, search in the right half
        else:
            return binary_search_recursive(arr, target, mid + 1, high)
    return -1  # Return -1 if target is not found

# Example usage (array should be sorted):
arr = [5, 10, 12, 24, 33, 89]
target = 33
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
