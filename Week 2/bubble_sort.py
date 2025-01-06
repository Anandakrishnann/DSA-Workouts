def bubble_sort(arr):
    """
    Perform Bubble Sort on the input array.
    
    Arguments:
    - arr: A list of unsorted elements.
    
    Returns:
    - The sorted list in ascending order.
    """
    n = len(arr)  # Get the length of the array
    
    # Outer loop to iterate over the array multiple times
    for i in range(n):
        swapped = False  # Track if any elements were swapped in this pass
        
        # Inner loop to compare adjacent elements
        for j in range(0, n - i - 1):
            # Swap if the current element is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Mark that a swap occurred

        # If no elements were swapped, the array is already sorted
        if not swapped:
            break

    return arr

# Example usage
arr = [1, 3, 5, 6, 34, 65, 2, 34, 56]  # Unsorted array
sorted_arr = bubble_sort(arr)  # Sort the array using Bubble Sort

# Print the sorted array
print("Sorted Array:", sorted_arr)
