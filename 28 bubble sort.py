# Concept:
# Repeatedly swaps adjacent elements if they are in the wrong order.
# After each pass, the largest element "bubbles up" to its correct position.
# Steps:
# Compare adjacent elements and swap if necessary.
# Continue for all elements.
# After each full pass, the last element is sorted.
# Repeat for the remaining unsorted elements.
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        swapped=False
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
                break
        return arr
arr=[2,6,3,2,4,8,9]
res=(bubble_sort(arr))  
print(res) 
                
