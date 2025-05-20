# Binary Search Algorithm
# The binary search works on sorted arrays and divides the search interval into 
# half after every comparison,
#  thus reducing the time complexity to O(log n). Here’s a step-by-step explanation of your code:
def binary_search(arr,target):
    left,right=0,len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
arr=[10,20,30,40,50]     
target=50
res=binary_search(arr,target)
print(res)       
