def product_of_last_three(arr):
    if arr[0]>arr[1]:
        max1,max2=arr[0],arr[1]
    else:
        max1,max2=arr[1],arr[0]
    max3=arr[2]
    if max3>max1:
        max1,max2,max3=max3,max1,max2
    elif max3>max2:
        max2,max3=max3,max2
    for i in range(3,len(arr)):
        if arr[i]>max1:
            max3=max2
            max2=max1
            max1=arr[i]
        elif arr[i]>max2:
            max3=max2
            max2=arr[i]     
        elif arr[i]>max3:
            max3=arr[i]
    return max1*max2*max3
arr=[1,2,3]
res=product_of_last_three(arr)
print(res)

    
# finding third largest element in an array
def third_largest(arr):
    n=len(arr)
    first=float('-inf')
    for i in range(n):
        if arr[i]>first:
            first=arr[i]
    second=float('-inf')
    for i in range(n):
        if arr[i]>second and arr[i]<first:
            second=arr[i]
    third=float('-inf')
    for i in range(n):
        if arr[i]>third and arr[i]<second:
            third=arr[i]
    return third
arr=[1,3,4,2,6,7,8,9]
print(third_largest(arr))                         

# Adding one to number represented as array of digits
# Last Updated : 13 Feb, 2025
# Given a non-negative number represented as an array of digits. The is to add 1 to the number (increment the number represented by the digits by 1). The digits are stored such that the most significant digit is the first element of the array.
# Input : [1, 2, 4]
# Output : 125
# Explanation: 124 + 1 = 125 
# Input : [9, 9, 9]
# Output: 1000
# Explanation: 999 + 1 = 1000 
def addone(digits):
    n=len(digits)
    for i in range(n-1,-1,-1):
        if digits[i]<9:
            digits[i]+=1
            break
        digits[i]=0
    else:
        digits=[1]+digits
    result=int(''.join(map(str,digits)))    
    return result
digits=[1,2,3]
print(addone(digits))  

# Stock Buy and Sell - Max one Transaction Allowed
# Input: prices[] = {7, 10, 1, 3, 6, 9, 2}
# Output: 8
# Explanation: Buy for price 1 and sell for price 9. 
def busell(stocks):
    n=len(stocks)
    res=0
    for i in range(n-1):
        for j in range(i+1,n):
            res=max(res,stocks[j]-stocks[i])
    return res
stocks=[7, 10, 1, 3, 6, 9, 2] 
print(busell(stocks))        

# Finding sum of digits of a number until sum becomes single digit
# Input: n = 1234 
# Output: 1 
# Explanation:
# Step 1: 1 + 2 + 3 + 4 = 10 
# Step 2: 1 + 0 = 1
def sum_digits(n):
    while n>=10:
        temp=0
        while n>0:
            temp+=n%10
            n=n//10
        n=temp
    return n
n=1234
print(sum_digits(n))    

# Rearrange Array Elements by Sign
# Input:  arr[] = [1, 2, 3, -4, -1, 4]
# Output: arr[] = [1, -4, 2, -1, 3, 4]
def rearrange(nums):
    n=len(nums)
    res=[0]*n
    pos_index=0
    neg_index=1
    for i in range(n):
        if nums[i]>0:
            res[pos_index]=nums[i]
            pos_index+=2
        else:
            res[neg_index]=nums[i]
            neg_index+=2    
    return res
nums=[1,4,-3,6,-2,-7]
print(rearrange(nums))        