# Selection Sort works by repeatedly selecting the smallest element from the unsorted part of
#  the array and swapping it with the first unsorted element 
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
arr=[4,2,6,8,9]
res=selection_sort(arr)
print(res)       