def selection_sort(arr):
    """
    Perform selection sort on the given array.
    Sorts the array in ascending order.
    """
    # Outer loop iterates through each element in the array except the last one
    for i in range(len(arr) - 1):
        # Inner loop checks all elements after the current index `i`
        for j in range(i + 1, len(arr)):
            # Compare the current element with subsequent elements
            if arr[i] > arr[j]:
                # Swap elements if the current element is greater
                arr[i], arr[j] = arr[j], arr[i]


# Example usage
arr = [4, 3, 56, 75, 4, 6, 7, 5, 4, 2]  # Input array
selection_sort(arr)  # Sort the array
print(arr)  # Print the sorted array
