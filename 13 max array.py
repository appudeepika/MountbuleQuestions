# finding max element in array
def find_max(arr):
    max=arr[0]
    for i in arr:
        if i>max:
            max=i
    print(f"the max number is {max}")
arr=[3,4,5,6,2,7,8]
find_max(arr)     

# finding max and min element in array
def find_max_min(arr):
    max=arr[0]
    min=arr[0]
    for i in arr:
        if i>max:
            max=i
        elif i<min:
            min=i
    print(f"the max number is {max}")  
    print(f"the min number is {min}")      
arr=[3,4,5,6,2,7,8]
find_max_min(arr)     

# taking input and adding to the array and finding max and min
def find_max_min(arr_size):
    array=[]
    for i in range(arr_size):
        num=int(input("enter nmbr:"))
        array+=[num]
    print(array)
    max=array[0]
    min=array[0]
    for num in array:
        if i>max:
            max=i
        if i<min:
            min=i
    print(f"the maximum number is {max}")
    print(f"the min number is {min}")
arr_size=int(input("enter the range"))
find_max_min(arr_size)                

