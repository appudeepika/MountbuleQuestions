# Reverse an Array in groups of given size
def reverse_array_gropus(arr,k):
    for i in range(0,len(arr),k):
        start=i
        end=(i+k-1,len(arr)-1)
        while start < end:
            arr[start],arr[end]=arr[end],arr[start]
            start+=1
            end-=1
    return arr
arr=[1,2,3,4,5,6,7,8,9]   
k=3
res=reverse_array_gropus(arr,k)
print(res)
