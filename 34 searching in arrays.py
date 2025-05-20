# Searching in Arrays
# 1)Linear Search in an array
# 2)Binary Search in a sorted array
# 3)Find the first occurrence of an element
# 4)Find the last occurrence of an element
# 5)Count the frequency of each element

# 1)Linear Search in an array:
# Linear Search is a simple searching algorithm used to find an element in a list or array
#  by checking each element one by one from the beginning to the end until the target value 
#  is found or the list is fully traversed.
# When the list is unsorted.
# When the list is small.
# When there is no additional information about the data structure
# -->works on unsorted array
def linear_serach(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
arr=[10,20,30,40,50]
target=50
res=linear_serach(arr,target)
if res!=-1:
    print(f"the element found at index {res}")
else:
    print("element not found")    
  

# 2)Binary Search in a sorted array
# Binary Search is an efficient searching algorithm used to find an element in a sorted list or array.
# It works by repeatedly dividing the search space in half until the target element is found or
# the search space is empty.
# -->works on sorted array
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
arr=[2,3,4,5,6,7]
target=2
res=binary_search(arr,target)
print(f"the index of the given target is {res}")

# 3)Find the first occurrence of an element
def first_occurance(arr,target):
    for i in arr:
        if arr[i]==target:
            return i
    return -1
arr=[2,3,4,5,5,6,8]
target=5
res=first_occurance(arr,target)
if res!=target:
    print(f"the index of target is {res}")  
else:
    print("not  found")    

# 4)Find the last occurrence of an element
def first_occurance(arr,target):
    last_index=-1
    for i in range(len(arr)):
        if arr[i]==target:
            last_index=i
    return last_index
arr=[2,3,4,5,5,6,8]
target=5
res=first_occurance(arr,target)
if res!=target:
    print(f"the index of target is {res}")  
else:
    print("not  found")    

#  5)Count the frequency of each element
def frequence_occurance(arr):
    freq={}
    for num in arr:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1
    return freq 
arr=[1,2,3,2,3,4,5,6,5,6,7,7,5]
res=frequence_occurance(arr)
print(res)           






