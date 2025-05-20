# ROTATE AN ARRAY
def leftrotate(arr,d,n):
    for x in range(d):
        rotateone(arr,n)
def rotateone(arr,n):
    temp=arr[0]
    for j in range(n-1):
        arr[j]=arr[j+1]
    arr[n-1]=temp
arr=[1,2,3,4,5,6]
leftrotate(arr,3,6)
print(arr)

# 
def rotate(arr,d,n):
    for _ in range(d):
        temp=arr[0]
        for i in range(n-1):
            arr[i]=arr[i+1]
        arr[n-1]=temp
arr=[1,2,3,4,5,6]
d=2
n=len(arr)
rotate(arr,d,n)      
print(arr)      
