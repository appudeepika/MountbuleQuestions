# Sorting in Arrays
# 1)Bubble Sort
# 2)Selection Sort
# 3)Insertion Sort
# 4)Merge Sort
# 5)Quick Sort

# BUBBLE SORT:Bubble Sort is a simple sorting algorithm that repeatedly swaps adjacent elements if they 
# are in the wrong order. This process is repeated until the list is sorted.
def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[2,6,1,8,9,4,5]
res=bubble_sort(arr)
print(res)            
