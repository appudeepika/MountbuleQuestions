# BASIC ARRAY OPERATORS
# 1)Insert an element at a specific position
def insert_position(arr,element,position):
    new_arr=[0]*(len(arr)+1)
    for i in range(position):
        new_arr[i]=arr[i]
        new_arr[position]=element
        for i in range(position,len(arr)):
            new_arr[i+1]=arr[i]
    return new_arr
arr=[10,20,30,40,50]
element=5
position=2
res=insert_position(arr,element,position)
print(res)        

# INSERTING AT MULTIPLE POSITIONS
def insert_position(arr,element1,element2,position1,position2):
    new_arr=[0]*(len(arr)+1)
    for i in range(position):
        new_arr[i]=arr[i]
        new_arr[position1]=element1
        new_arr[position2]=element2
        for i in range(position2,len(arr)):
            new_arr[i+1]=arr[i]
    return new_arr
arr=[10,20,30,40,50]
element1=5
position1=2
element2=4
position2=3
res=insert_position(arr,element1,element2,position1,position2)
print(res)        

# Delete an element from an array
def delete_element(arr,element):
    position=-1
    for i in range(len(arr)):
        if arr[i]==element:
            position=i
            break
    if position==-1:
        return arr
    new_arr=[0]*(len(arr)-1)
    for i in range(position):
        new_arr[i]=arr[i]
    for i in range(position+1,len(arr)):
        new_arr[i-1]=arr[i]
    return new_arr
arr=[10,20,30,40,50]
element=40
res=delete_element(arr,element)
print(res)            


# FIND THE LARGEST ELEMENT IN AN ARRAY
def largest_element(arr):
    max=arr[0]
    for i in range(len(arr)):
        if arr[i]>max:
            max=arr[i]
    return max
arr=[10,3,2,5,7,30,70]
res=largest_element(arr)
print(f"the largest element is {res}")        

# FIND THE SMALLEST ELEMENT IN AN ARRAY
def largest_element(arr):
    min=arr[0]
    for i in range(len(arr)):
        if arr[i]<min:
            min=arr[i]
    return min
arr=[10,3,2,5,7,30,70]
res=largest_element(arr)
print(f"the smallest element is {res}")  

# 5)Find the second largest element
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
arr=[2,5,3,7,8]
res=second_largest(arr)
print(f"The second largest element in tha given array is {res}")  

# Find the second smallest element


def second_smallest(arr):
    if arr[0]<arr[1]:
        min1,min2=arr[0],arr[1]
    else:
        min1,min2=arr[1],arr[0]
        for i in range(len(arr)):
            if arr[i]<min1:
                min2=min1
                min1=arr[i]
            elif arr[i]<min2:
                min2=arr[i]
    return min2
arr=[4,3,2]
res=second_smallest(arr)
print(f"the second smallest element in the given array is {res}")

# Reverse an array
def reverse(arr):
    mid=len(arr)//2
    for i in range(mid):
        arr[i],arr[len(arr)-i-1]=arr[len(arr)-i-1],arr[i]
    print(arr)
arr=[10,2,3,4,5]
reverse(arr)   

# 8)Left rotate an array by one position
def left_rotate(arr):
    n=len(arr)
    first_element=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=first_element
    return arr
arr=[1,2,3,4,5]
res=left_rotate(arr)
print(res)     

# 9)Right rotate an array by one position

def rotate_right(arr):
    n=len(arr)
    lastelement=arr[n-1]
    for i in range(n-1):
        arr[i],arr[i+1]
    arr[n-1]=lastelement
arr=[1,2,3,4,5]
res=rotate_right(arr)
print(res)  

# Left rotate an array by ‘k’ positions
def left_array(arr,k):
    n=len(arr)
    k=k%n
    arr[:]=arr[k:]+arr[:k]
    return arr
arr=[1,2,3,4,5,6]
k=2
res=left_array(arr,k)
print(res)    

def left_array(arr,d):
    n=len(arr)
    for _ in range(d):
        temp=arr[0]
        for i in range(n-1):
            arr[i]=arr[i+1]
        arr[n-1]=temp
    return arr
arr=[1,2,3,4,5]
d=2
res=left_array(arr,d)
print(res)        

# Right rotate an array by ‘k’ positions   
def left_array(arr,d):
    n=len(arr)
    for _ in range(d):
        temp=arr[-1]
        for i in range(n-1,0,-1):
            arr[i]=arr[i-1]
        arr[0]=temp
    return arr
arr=[1,2,3,4,5]
d=2
res=left_array(arr,d)
print(res)        

# 12)Copy elements from one array to another 
def copy_elements(arr1):
    arr2=[]
    for i in range(len(arr1)):
        arr2.append(arr1[i])
    return arr2
arr1=[1,2,3,4,5]
res=copy_elements(arr1)
print(res)     