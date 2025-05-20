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

    