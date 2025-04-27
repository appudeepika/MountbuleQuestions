Two Pointer & Sliding Window Problems
1)Find the longest subarray with sum ≤ K
2)Find the smallest subarray with a sum greater than a given value
3)Find the first repeating element in an array
4)Find the first non-repeating element in an array

# Maximum Sum of a Subarray of Size K (Fixed Window)

# 1. Maximum Sum Subarray of Size K
def max_sum(arr,k):
    n=len(arr)
    window_sum=0
    for i in range(k):
        window_sum+=arr[i]
    max_sum=window_sum   
    for i in range(k,n): 
        window_sum=window_sum-arr[i-k]+arr[i]
        if window_sum>max_sum:
            max_sum=window_sum
    return max_sum        
arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum(arr, k)) 