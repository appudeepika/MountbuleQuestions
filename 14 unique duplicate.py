def find_unique_duplicate(array):
    unique=[]
    duplicate=[]
    for i in array:
        if i not in array:
            unique.append(i)
        else:
            duplicate.append(i)
        return unique,duplicate 
array=[1,2,3,2,3,2,3,4,5,5,6,7,7,8]   
unique,duplicate=find_unique_duplicate(array)     
print(unique)
print(duplicate)      