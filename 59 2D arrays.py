# Creating a 2D Array
array=[
    [1,2,3],
    [4,5,6],
    [7,4,9]]
for i in array:
    print(i)

#Assecing elements
arr=[
    [1,2,3],
    [6,7,5],
    [8,9,5]]
print(arr[0][2])
print(arr[1][0])

# Modifying Elements
arr=[
    [1,2,3],
    [6,7,5],
    [8,9,5]]
arr[2][1]=100
arr[2][2]=200
for i in arr:
    print(i)

#Iterating Over a 2D Array 
arr=[
    [1,2,3],
    [6,7,5],
    [8,9,5]]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(f"the elements of ({i},{j})={arr[i][j]}")
# Slicing a 2D Array
arr=[
    [1,2,3],
    [6,7,5],
    [8,9,5]]
print(arr[:2])
print([row[0] for row in arr])
print([row[1] for row in arr])
# Creating a 2D Array Dynamically
rows,col=4,4
ar=[[1 for _ in range(col)] for _ in range(rows)]
for row in ar:
    print(row)
