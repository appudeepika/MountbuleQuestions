# Extract a Subarray (Without Slicing)
def subarray(arr,l,r):
    subarr=[]
    for i in range(l,r+1):
        subarr.append(arr[i])
    return subarr 
arr=[1,2,3,4,5,6,7]
l=2
r=5
res=subarray(arr,l,r)
print(res)   


# Exercise 2: Print All Subarrays (Without Slicing)
def subarray(arr):
    n=len(arr)
    allsubarr=[]
    for i in range(n):
        for j in range(i,n):
            subarr=[]
            for k in range(i,j+1):
                subarr.append(arr[k])
            allsubarr.append(subarr)    
    return allsubarr
arr=[1,2,3]
res=subarray(arr)
print(res)            

-->subarr is a temporary list that holds a single subarray.
-->allsubarr is the main list that stores all subarrays.
-->Every subarr is added to allsubarr once completed.
-->Final result contains all possible contiguous subarrays.

# Find Maximum Sum of a Subarray (Brute Force)
def max_sum(arr):
    n=len(arr)
    max_sum=arr[0]
    for i in range(n):
        for j in range(i,n):
            sub_sum=0
            for k in range(i,j+1):
                sub_sum+=arr[k]
            if sub_sum>max_sum:
                max_sum=sub_sum
    return max_sum
arr= [-2, 1, -3, 4, -1, 2, 1, -5, 4]    
res=max_sum(arr)
print(res)  

# COUNT ALL SUNSTRING
def count_substring(arr):
    n=len(arr)
    count=0
    for i in range(n):
        for j in range(i,n):
            count+=1
    return count   
arr=[1,2,3]
res=count_substring(arr)
print(res)     

#  Find All Subarrays With Given Sum
def sun_array_with_given_sum(arr,terget):
    n=len(arr)
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=arr[j]
            if sum==terget:
                print(arr[i:j+1])  
arr=[1,2,3,4,5]
terget=5
sun_array_with_given_sum(arr,terget)

# Check If Any Subarray Has Zero Sum
def has_zero_sum_subarray(arr):
    n = len(arr)
    
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum == 0:
                return True
    return False

arr = [4, 2, -3, 1, 6]
print(has_zero_sum_subarray(arr))  # Output: True

  