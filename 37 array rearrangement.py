# Array Rearrangement Problems
# 1)Move all zeros to the end of the array
# 2)Move all negative numbers to one side of the array
# 3)Rearrange the array such that even numbers come first, then odd numbers
# 4)Segregate 0s and 1s in a binary array
# 5)Rearrange an array in alternating positive and negative numbers

# 1)Move all zeros to the end of the array
def move_zeros_end(arr):
    n=len(arr)
    count=0
    for i in range(n):
        if arr[i]!=0:
            arr[count]=arr[i]
            count+=1
    while count<n:
        arr[count]=0
        count+=1
    return arr
arr=[0,1,3,4,0,6,0,4,8,0]
res=move_zeros_end(arr)
print(res)      

# 2)Move all negative numbers to one side of the array
def move_negative_nmbrs(arr):
    positive=[]
    negative=[]
    for i in arr:
        if i>0:
            positive.append(i)
        else:
            negative.append(i)
    return positive+negative
arr=[2,5,-3,6,-7,9]
res=move_negative_nmbrs(arr)
print(res)    

def move_negatives_to_end(arr):
    n = len(arr)
    count = 0 
    for i in range(n):
        if arr[i] >= 0:
            arr[count], arr[i] = arr[i], arr[count]  
            count += 1  
    return arr 
arr = [1, 5, -2, 6, 7, -4, 9, -7]
result = move_negatives_to_end(arr)
print(result) 


# 3)Rearrange the array such that even numbers come first, then odd numbers
def even_odd(arr):
    even=[]
    odd=[]
    for i in arr:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return even+odd
arr=[2,3,4,5,6,7,8]   
res=even_odd(arr)
print(res) 


def even_odd(arr):
    n=len(arr)
    count=0
    odd=[]
    for i in range(n):
        if arr[i]%2==0:
            arr[count]=arr[i]
            count+=1
        else:
            odd.append(arr[i])
    for i in range(len(odd)):
        arr[count]=odd[i]
        count+=1              
    return arr         
arr=[2,3,4,5,6,7,8]   
res=even_odd(arr)
print(res)       

# 4)Segregate 0s and 1s in a binary array
def zeros_ones(arr):
    n=len(arr)
    count=0
    odd=[]
    for i in range(n):
        if arr[i]==0:
            arr[count]=arr[i]
            count+=1
    while count<n:
        arr[count]=1
        count+=1                     
    return arr         
arr=[0,1,0,1,0,0,1,1,0,1]   
res=zeros_ones(arr)
print(res)          

# 5)Rearrange an array in alternating positive and negative numbers