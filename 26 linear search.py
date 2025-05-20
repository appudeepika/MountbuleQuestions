# Linear search is the simplest search algorithm. It works by checking each element of the array one by one,
#  starting from the first element, and continuing until 
# either the target is found or the end of the array is reached.
def linear_serach(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
arr=[10,20,30,40,50]
target=40
res=linear_serach(arr,target)
if res!=-1:
    print(f"target {target} found at index {res}")
else:
    print(f"target{target} not found")    


