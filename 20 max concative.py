def max_concutive_ones(arr):
    max_streak=0
    current_streak=0
    for i in range(len(arr)):
        if arr[i]==1:
            current_streak+=1
        else:
            current_streak=0
        if current_streak>max_streak:
            max_streak=current_streak
    return max_streak      
arr=[1,0,1,1,1,1,1,0,1,0,0]
res=max_concutive_ones(arr)
print(res)             

