def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Choose the middle element as pivot
    left = [x for x in arr if x < pivot]  # Subarray with elements smaller than the pivot
    middle = [x for x in arr if x == pivot]  # Subarray with elements equal to the pivot
    right = [x for x in arr if x > pivot]  # Subarray with elements larger than the pivot
    return quick_sort(left) + middle + quick_sort(right)
print(quick_sort([5, 3, 8, 1, 2]))



# Quick Sort Algorithm
# Quick Sort is an efficient divide-and-conquer sorting algorithm that works by selecting a pivot element and partitioning the array into two smaller subarrays: one with elements smaller than the pivot and one with elements greater than the pivot. Then, the algorithm recursively sorts the subarrays.

# Key Concepts:
# Pivot Selection: Choose an element from the array (typically the first element, the last element, or a random element) as the "pivot."
# Partitioning: Rearrange the array so that elements smaller than the pivot come before it, and elements greater than the pivot come after it.
# # Recursion: Recursively apply the same process to the left and right subarrays formed after partitioning.