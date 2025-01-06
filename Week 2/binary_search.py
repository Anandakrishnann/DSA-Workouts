def binary_search(arr, target):
    """
    Perform a binary search on a sorted array to find the target element.
    
    Arguments:
    - arr: A list of sorted elements.
    - target: The element to search for.
    
    Returns:
    - The index of the target element if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1  # Initialize the search boundaries (start and end indices)
    
    # Loop until the search space is empty
    while left <= right:
        # Calculate the middle index
        mid = (left + right) // 2
        
        # Check if the middle element is the target
        if arr[mid] == target:
            return mid  # Target found, return its index
        elif arr[mid] < target:
            # If the target is greater than the middle element, search the right half
            left = mid + 1
        else:
            # If the target is smaller than the middle element, search the left half
            right = mid - 1

    # If the loop ends, the target was not found
    return -1

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8]  # Sorted array to search
target = 6  # Target element to find

# Perform binary search and print the result
result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the array.")
