# Missing and Repeating in an Array
# Last Updated : 20 Aug, 2024
# Given an unsorted array of size n. Array elements are in the range of 1 to n. One number from set {1, 2, …n} is missing and one number occurs twice in the array. Find these two numbers.

# Examples: 

# Input: arr[] = {3, 1, 3}
# Output: Missing = 2, Repeating = 3
# Explanation: In the array, 2 is missing and 3 occurs twice 


# Input: arr[] = {4, 3, 6, 2, 1, 1}
# Output: Missing = 5, Repeating = 1

def finding_missing_repeating(arr,n):
    arr.sort()
    repeating=None
    missing=None
    for i in range(n-1):
        if arr[i]==arr[i+1]:
            repeating=arr[i]
    for i in range(1,n+1):
        if i not in arr:
            missing=i
            break       
    print(f"missing={missing},repeating={repeating}")   
arr=[1,2,3]
n=len(arr)   
finding_missing_repeating(arr,n) 