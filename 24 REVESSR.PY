# REVERSE OF AN ARRAY
def reverse_array(arr):
    mid=len(arr)//2
    for i in range(mid):
        arr[i],arr[len(arr)-i-1]=arr[len(arr)-i-1],arr[i]
    print(arr)
arr=[1,2,3,4,5]
reverse_array(arr)        



# Remove All Occurrences of an Element in an Array
def count_array(arr):
    newarr=[]
    count=0
    for i in arr:
        if i not in newarr:
            newarr.append(i)
            count+=1
    print(newarr)
    print(count)
arr=[1,2,3,2,3,4,1,5,6,7]
count_array(arr)  