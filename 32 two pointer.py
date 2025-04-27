# The two-pointer technique is often used in problems where you need to iterate over an array in two different directions or with two indices to solve a problem efficiently. It is typically applied in situations like finding pairs in a sorted array, partitioning an array, or finding specific conditions in a given array.
def two_pointer(arr,target):
    left=0
    right=len(arr)-1
    while left<right:
        sum=arr[left]+arr[right]
        if sum==target:
            return arr[left],arr[right]
        elif sum<target:
            left+=1
        else:
            right-=1
    return None
arr=[1,2,3,4,5,6,7,8,9]
target=9
res=two_pointer(arr,target)
print(res)           