def merge_sort(arr):
    """
    Perform merge sort on the input array.
    This is a divide-and-conquer algorithm that splits the array into halves,
    recursively sorts them, and merges them back together.
    """
    # Base case: if the array has more than one element, proceed
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle point of the array

        # Split the array into two halves
        left_half = arr[:mid]  # Left sub-array
        right_half = arr[mid:]  # Right sub-array

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Initialize pointers for merging
        i = j = k = 0  # i for left_half, j for right_half, k for the main array

        # Merge the two halves into the original array in sorted order
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]  # Take the smaller element from left_half
                i += 1
            else:
                arr[k] = right_half[j]  # Take the smaller element from right_half
                j += 1
            k += 1  # Move to the next position in the main array

        # Copy any remaining elements from left_half, if any
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy any remaining elements from right_half, if any
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        # Return the array (not necessary, but helps with understanding)
        return arr


# Example array to be sorted
arr = [3, 8, 5, 1, 4, 7, 2, 6]

# Sort the array using merge sort
merge_sort(arr)

# Print the sorted array
print(arr)
