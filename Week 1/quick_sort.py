def quick_sort(arr,low, high):
    if low < high:
        
        pi = partition(arr, low, high)
        
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)
    
    return arr

def partition(arr, low, high):
    if low < high:
        mid = (low+high)//2
        pivot = arr[mid]
        
        arr[mid],arr[high] = arr[high],arr[mid]
        
        i = low-1
        
        for j in range(low,high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i+1],arr[high] = arr[high],arr[i+1]
        return i + 1

arr = [34,56,23,65,21]
n = len(arr)
quick_sort(arr,0,n-1)
print("Sorted Array",arr)