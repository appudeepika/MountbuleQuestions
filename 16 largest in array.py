# prohram to find largest nmbr in an array
def find_largest(arr):
    large=arr[0]
    for i in arr:
        if i>large:
            large=i
    print(large)
arr=[10,20,80,4,5,6]
find_largest(arr)            
