# sum of array
def find_sum(arr):
    sum=0
    for i in arr:
        sum=sum+i
    print(sum)
arr=[1,2,3,4]
find_sum(arr)        

def find_sum(arr_size):
    array=[]
    sum=0
    for i in range(arr_size):
        n=int(input("enter nmbr:"))
        array.append(n)
    print(array)    
    for i in array:
        sum=sum+i
    print(sum)
arr_size=int(input("enter the target nmbr:"))
find_sum(arr_size)            
