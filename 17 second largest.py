def second_largest(arr):
    if arr[0]>arr[1]:
        max1,max2=arr[0],arr[1]
    else:
        max1,max2=arr[1],arr[0]
    for i in range(len(arr)):
        if arr[i]>max1:
            max2=max1
            max1=arr[i]
        elif arr[i]>max2:
            max2=arr[i]
    return max2
arr=[2,4,3,5,6,7]
res=second_largest(arr)
print(f"The second largest element in tha given array is {res}")            
