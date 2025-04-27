# Subarray and Subset Problems
# 1)Find the subarray with the maximum sum (Kadane’s Algorithm)
# 2)Find the subarray with the minimum sum
# 3)Find all pairs in an array that sum to a given value
# 4)Find the equilibrium index in an array (sum of left = sum of right)
# 5)Check if an array contains a subset with a given sum

# 1)Find the subarray with the maximum sum (Kadane’s Algorithm)
def kadane_algorith(arr):
    max_sum=arr[0]
    current_sum=0
    for num in arr:
        current_sum+=num
        if current_sum>max_sum:
            max_sum=current_sum
        if current_sum<0:
            current_sum=0
    return max_sum    
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(kadane_algorith(arr))


# 2)Find the subarray with the minimum sum
def kadane_algorith_minimum_sum(arr):
    min_sum=arr[0]
    current_sum=0
    for num in arr:
        current_sum+=num
        if current_sum<min_sum:
            min_sum=current_sum
        if current_sum>0:
            current_sum=0
    return min_sum    
arr =[3, -4, 2, -3, -1, 7, -5]
print(kadane_algorith_minimum_sum(arr))
       
# 3)Find all pairs in an array that sum to a given value
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
       
# 4)Find the equilibrium index in an array (sum of left = sum of right)
Finding the Equilibrium Index in an Array
An equilibrium index is an index in the array where the sum of elements on the left is equal to the sum of elements on the right.
