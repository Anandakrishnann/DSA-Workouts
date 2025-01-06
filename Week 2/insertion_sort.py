def insertion_sort(arr):
    """
    Perform insertion sort on the input array.
    Sorts the array in ascending order.
    """
    # Start with the second element (index 1) since the first element is trivially sorted
    for i in range(1, len(arr)):
        key = arr[i]  # The current element to be placed in the sorted part of the array
        j = i - 1  # Index of the last sorted element

        # Shift elements of the sorted part of the array to the right 
        # if they are greater than the key
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # Move the larger element one position to the right
            j -= 1  # Move to the previous element

        # Place the key at the correct position in the sorted part of the array
        arr[j + 1] = key

    return arr  # Return the sorted array


# Example array to be sorted
arr = [1, 34, 67, 89, 66, 55, 4, 2, 3]

# Sort the array using insertion sort
res = insertion_sort(arr)
