def move_zeros_end(arr):
    non_zeros=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[i],arr[non_zeros]=arr[non_zeros],arr[i]
            non_zeros+=1
    return arr
arr=[1,0,34,0,56,0]
res=move_zeros_end(arr)
print(res)        
