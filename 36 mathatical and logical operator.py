# Mathematical & Logical Operations
# 1)Find the sum of all positive numbers in an array
# 2)Find the sum of all negative numbers in an array
# 3)Check if an array is sorted (ascending or descending)
# 4)Find the product of all elements in an array
# 5)Find the missing number in an array (1 to N, N+1 elements given)
# 6)Find the duplicate element in an array
# 7)Find common elements between two arrays

# 1)Find the sum of all positive numbers in an array
def positive_nmbs(arr):
    sum=0
    for i in arr:
        if i>0:
            sum=sum+i
    return sum
arr=[-1,3,-5,3,6,7,-2]
res=positive_nmbs(arr)
print(res)    

# 2)Find the sum of all negative numbers in an array
def negative_nmbs(arr):
    sum=0
    for i in arr:
        if i<0:
            sum=sum+i
    return sum
arr=[-1,3,-5,3,6,7,-2]
res=negative_nmbs(arr)
print(res)    

# 3)Check if an array is sorted (ascending or descending)
# arrays is sorted or unsorted
def check_sorted_unsorted(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            print("array is unsorted")
            return
    print("array is sorted")
arr=[1,2,3,4,5]
res=check_sorted_unsorted(arr)
print(res)        

# 4)Find the product of all elements in an array
def product(arr):
    produ=1
    for i in arr:
        if i>0:
            produ=produ*i
    return produ
arr=[1,2,3,4]
res=product(arr)
print(res)        

# 5)Find the missing number in an array (1 to N, N+1 elements given)
def missing_nmbe(arr):
    n=len(arr)+1
    expected_sum=(n*(n+1))//2
    actual_sum=sum(arr)
    return expected_sum-actual_sum
arr=[1,2,3,5,6]
res=missing_nmbe(arr)
print(res)

# 6)Find the duplicate element in an array
def find_duplicates(arr):
    duplicates=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                if arr[i] not in duplicates:
                    duplicates.append(arr[i])
    return duplicates
arr=[2,3,4,5,6,7,8,4,9,2,5,6]
res=find_duplicates(arr)
print(res)     

# find the unique elements in an array
def find_unique(arr):
    unique=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]!=arr[j]:
                if arr[i] not in unique:
                    unique.append(arr[i])
    return unique
arr=[2,3,4,5,6,7,8,4,9,2,5,6]
res=find_unique(arr)
print(res)    

# 7)Find common elements between two arrays
def common_elements(arr1,arr2):
    common=[]
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i]==arr2[i]:
                if arr2[i] not in common:
                    common.append(arr2[i])
    return common
arr1=[2,3,4,5,6]
arr2=[2,3,7,8,9]
res=common_elements(arr1,arr2)
print(res)                
